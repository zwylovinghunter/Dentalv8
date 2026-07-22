import cv2
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os
from pathlib import Path
from tkinter import Tk, filedialog


def choose_image_file():
    root = Tk()
    root.withdraw()
    root.update()
    image_path = filedialog.askopenfilename(
        title="选择牙齿影像图片",
        filetypes=[
            ("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.tif;*.tiff"),
            ("All files", "*.*"),
        ],
    )
    root.destroy()
    return image_path


def infer_label_path(image_path):
    path = Path(image_path)
    parts = list(path.parts)
    if "images" in parts:
        idx = parts.index("images")
        parts[idx] = "labels"
        return str(Path(*parts).with_suffix(".txt"))
    return str(path.with_suffix(".txt"))

def view_dental_xray(image_path, label_path, class_names=None):
    # 1. 检查文件是否存在
    if not os.path.exists(image_path):
        print(f"错误：找不到图片 {image_path}")
        return

    # 2. 读取图片 (OpenCV默认BGR，转为RGB给Matplotlib使用)
    img = cv2.imread(image_path)
    if img is None:
        print("图片读取失败")
        return
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    h, w, _ = img.shape

    # 3. 设置类别名称
    if class_names is None:
        class_names = {0: "Caries"}

    # 4. 创建画布
    # figsize 可以指定窗口初始大小，这里设为 15x7 英寸比较适合全景片
    fig, ax = plt.subplots(figsize=(15, 7))
    ax.imshow(img)

    # 5. 读取并绘制标注
    if os.path.exists(label_path):
        with open(label_path, 'r') as f:
            lines = f.readlines()

        for line in lines:
            parts = line.strip().split()
            if len(parts) != 5: continue
            
            cls_id = int(parts[0])
            x_c, y_c, bw, bh = map(float, parts[1:])

            # 还原坐标
            x1 = (x_c - bw / 2) * w
            y1 = (y_c - bh / 2) * h
            box_w = bw * w
            box_h = bh * h

            # 创建矩形框 (红色)
            rect = patches.Rectangle((x1, y1), box_w, box_h, linewidth=2, 
                                     edgecolor='r', facecolor='none')
            ax.add_patch(rect)

            # 添加文字标签
            label_text = class_names.get(cls_id, f"ID:{cls_id}")
            plt.text(x1, y1 - 10, label_text, color='red', 
                     fontsize=10, fontweight='bold', backgroundcolor='white')
    else:
        print("未找到标注文件，仅显示原图。")

    plt.title(f"Dental Detection - {os.path.basename(image_path)}\n(Use the magnifying glass tool to zoom)", fontsize=12)
    plt.axis('off')  # 隐藏坐标轴
    print("提示：使用窗口下方的'放大镜'图标可以局部放大牙齿细节。")
    plt.tight_layout()
    plt.show()

# --- 使用示例 ---
if __name__ == "__main__":
    img_path = choose_image_file()
    if not img_path:
        print("未选择图片，程序已退出。")
        raise SystemExit

    txt_path = infer_label_path(img_path)
    print(f"已选择图片：{img_path}")
    print(f"自动匹配标注：{txt_path}")

    class_names = {0: "Caries", 1: "Periapical Lesion", 2: "Impacted"}
    view_dental_xray(img_path, txt_path, class_names)
