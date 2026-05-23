# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license
"""Dental lesion ablation modules."""

from __future__ import annotations

import torch
import torch.nn as nn
import torch.nn.functional as F

from .conv import Conv
from .head import Detect


class SPDConv(nn.Module):
    """Space-to-depth downsampling followed by stride-1 Conv."""

    def __init__(self, c1: int, c2: int, k: int = 3):
        super().__init__()
        self.conv = Conv(c1 * 4, c2, k, 1)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        if x.shape[-2] % 2 or x.shape[-1] % 2:
            x = F.pad(x, (0, x.shape[-1] % 2, 0, x.shape[-2] % 2))
        x = torch.cat(
            (
                x[..., 0::2, 0::2],
                x[..., 1::2, 0::2],
                x[..., 0::2, 1::2],
                x[..., 1::2, 1::2],
            ),
            dim=1,
        )
        return self.conv(x)


class GatedSPDConvDown(nn.Module):
    """Baseline downsampling plus a learnable weak SPDConv residual branch."""

    def __init__(self, c1: int, c2: int, k: int = 3, gamma_init: float = 0.05):
        super().__init__()
        self.conv_down = Conv(c1, c2, k, 2)
        self.spd_down = SPDConv(c1, c2, k)
        self.gamma = nn.Parameter(torch.tensor(float(gamma_init)))

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.conv_down(x) + self.gamma * self.spd_down(x)


class HybridSPDConvDown(nn.Module):
    """Half baseline downsampling and half SPDConv downsampling, concatenated on channels."""

    def __init__(self, c1: int, c2: int, k: int = 3):
        super().__init__()
        c_conv = c2 // 2
        c_spd = c2 - c_conv
        self.conv_down = Conv(c1, c_conv, k, 2)
        self.spd_down = SPDConv(c1, c_spd, k)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return torch.cat((self.conv_down(x), self.spd_down(x)), dim=1)


class CoordAtt(nn.Module):
    """Coordinate attention with unchanged tensor shape."""

    def __init__(self, c1: int, reduction: int = 32):
        super().__init__()
        mip = max(8, c1 // reduction)
        self.pool_h = nn.AdaptiveAvgPool2d((None, 1))
        self.pool_w = nn.AdaptiveAvgPool2d((1, None))
        self.conv1 = nn.Conv2d(c1, mip, 1, bias=False)
        self.bn1 = nn.BatchNorm2d(mip)
        self.act = nn.SiLU()
        self.conv_h = nn.Conv2d(mip, c1, 1, bias=True)
        self.conv_w = nn.Conv2d(mip, c1, 1, bias=True)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        identity = x
        _, _, h, w = x.shape
        x_h = self.pool_h(x)
        x_w = self.pool_w(x).permute(0, 1, 3, 2)
        y = torch.cat((x_h, x_w), dim=2)
        y = self.act(self.bn1(self.conv1(y)))
        x_h, x_w = torch.split(y, [h, w], dim=2)
        x_w = x_w.permute(0, 1, 3, 2)
        a_h = self.conv_h(x_h).sigmoid()
        a_w = self.conv_w(x_w).sigmoid()
        return identity * a_h * a_w


class DyHeadBlock(nn.Module):
    """Lightweight task/spatial feature refinement for P3/P4/P5."""

    def __init__(self, channels: tuple[int, ...], reduction: int = 16):
        super().__init__()
        self.local = nn.ModuleList(Conv(c, c, 3) for c in channels)
        self.spatial = nn.ModuleList(nn.Conv2d(c, 1, 1) for c in channels)
        self.task = nn.ModuleList(
            nn.Sequential(
                nn.AdaptiveAvgPool2d(1),
                nn.Conv2d(c, max(8, c // reduction), 1, bias=False),
                nn.SiLU(),
                nn.Conv2d(max(8, c // reduction), c, 1, bias=True),
            )
            for c in channels
        )
        self.gamma = nn.ParameterList(nn.Parameter(torch.zeros(1)) for _ in channels)

    def forward(self, x: list[torch.Tensor]) -> list[torch.Tensor]:
        out = []
        for i, xi in enumerate(x):
            y = self.local[i](xi)
            y = y * self.spatial[i](y).sigmoid() * self.task[i](y).sigmoid()
            out.append(xi + self.gamma[i] * y)
        return out


class ChannelSE(nn.Module):
    """Lightweight squeeze-excitation channel attention for one feature level."""

    def __init__(self, c1: int, reduction: int = 16):
        super().__init__()
        hidden = max(8, c1 // reduction)
        self.attn = nn.Sequential(
            nn.AdaptiveAvgPool2d(1),
            nn.Conv2d(c1, hidden, 1, bias=True),
            nn.SiLU(),
            nn.Conv2d(hidden, c1, 1, bias=True),
            nn.Sigmoid(),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return x * self.attn(x)


class ChannelAttDetect(Detect):
    """YOLO Detect head with per-level channel attention before prediction."""

    def __init__(self, nc: int = 80, reg_max=16, end2end=False, ch: tuple = (), reduction: int = 16):
        super().__init__(nc=nc, reg_max=reg_max, end2end=end2end, ch=ch)
        self.channel_attn = nn.ModuleList(ChannelSE(c, reduction) for c in ch)

    def forward(self, x: list[torch.Tensor]):
        x = [self.channel_attn[i](xi) for i, xi in enumerate(x)]
        return super().forward(x)


class DyHeadDetect(Detect):
    """YOLO Detect head with lightweight Dynamic Head refinement before Detect."""

    def __init__(self, nc: int = 80, reg_max=16, end2end=False, ch: tuple = (), repeats: int = 1):
        super().__init__(nc=nc, reg_max=reg_max, end2end=end2end, ch=ch)
        self.dyhead = nn.ModuleList(DyHeadBlock(tuple(ch)) for _ in range(repeats))

    def forward(self, x: list[torch.Tensor]):
        for block in self.dyhead:
            x = block(x)
        return super().forward(x)
