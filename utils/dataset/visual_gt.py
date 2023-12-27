from PIL import Image, ImageDraw
import os
import xml.etree.ElementTree as ET

# 输入路径
# jpeg_images_path = "data/dataset/smoke_1597/JPEGImages"
# annotations_path = "data/dataset/smoke_1597/Annotations"
# output_path = "data/dataset/smoke_1597/visual"
jpeg_images_path = "data/dataset/smoke_1507/val/images"
annotations_path = "data/dataset/smoke_1507/val/Annotations"
output_path = "data/dataset/smoke_1507/val/visual"

# 创建输出路径
if not os.path.exists(output_path):
    os.makedirs(output_path)

# 获取所有JPEG图像文件
jpeg_files = [f for f in os.listdir(jpeg_images_path) if f.endswith(('.jpg', '.jpeg', '.png', '.JPG', '.PNG'))]

for jpeg_file in jpeg_files:
    # 构建Annotations文件的路径
    annotation_file = os.path.join(annotations_path, f"{os.path.splitext(jpeg_file)[0]}.xml")

    # if not os.path.exists(annotation_file):
    #     print(f"Warning: Annotation file not found for {jpeg_file}. Skipping.")
    #     continue

    # 读取JPEG图像
    image_path = os.path.join(jpeg_images_path, jpeg_file)
    image = Image.open(image_path)

    # 检查图像是否带有透明通道，如果是则转换为RGB模式
    if image.mode == 'RGBA':
        image = image.convert('RGB')

    draw = ImageDraw.Draw(image)

    # 解析XML文件并绘制bounding box
    tree = ET.parse(annotation_file)
    root = tree.getroot()

    for obj in root.findall(".//object"):
        # 获取bounding box坐标信息
        bbox = obj.find(".//bndbox")
        xmin = int(bbox.find("xmin").text)
        ymin = int(bbox.find("ymin").text)
        xmax = int(bbox.find("xmax").text)
        ymax = int(bbox.find("ymax").text)

        # 绘制bounding box
        draw.rectangle([xmin, ymin, xmax, ymax], outline="red", width=2)

    # 保存可视化结果
    output_image_path = os.path.join(output_path, f"visual_{jpeg_file}")
    image.save(output_image_path)

print("可视化完成，结果保存在visual文件夹中。")
