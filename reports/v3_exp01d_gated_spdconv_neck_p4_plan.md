# Scheme 1D: Gated SPDConv Neck P4

Formula: `y = Conv_down(x) + gamma * SPDConv_down(x)`.

- `gamma_init = 0.05`
- `gamma` is learnable.
- Baseline backbone remains unchanged.
- P3 small-object branch remains unchanged.
- The gated module is placed only at neck/head P3->P4 downsampling.
