import os
from pathlib import Path

# 替换为你要处理的目录的路径
directory = "/path/to/your/directory"

# 考虑的图片格式
image_formats = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"}

# 编号计数器
counter = 1

# 遍历目录中的每个文件
for filename in os.listdir(directory):
    # 获取文件扩展名
    extension = Path(filename).suffix.lower()

    # 检查文件是否为图片
    if extension in image_formats:
        # 构建旧的和新的文件路径
        old_file_path = os.path.join(directory, filename)
        new_file_name = f"image_{counter:04}{extension}"  # 用零填充编号
        new_file_path = os.path.join(directory, new_file_name)

        # 重命名文件
        os.rename(old_file_path, new_file_path)
        print(f"Renamed {filename} to {new_file_name}")

        # 增加计数器
        counter += 1
