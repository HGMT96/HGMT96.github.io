from PIL import Image

def convert_black_to_white(input_path, output_path):
    # 打开图片
    img = Image.open(input_path)

    # 获取图片的像素数据
    pixels = img.load()

    # 图片的宽度和高度
    width, height = img.size

    # 循环遍历每个像素
    for i in range(width):
        for j in range(height):
            # 获取当前像素的颜色值
            color = pixels[i, j]

            # 如果颜色接近黑色，则将其转换为白色
            if sum(color) < 30:  # 对颜色值求和来判断是否接近黑色
                pixels[i, j] = (255, 255, 255)  # 转换为白色

    # 保存修改后的图片
    img.save(output_path)

# 输入图片路径和输出图片路径
input_image_path = "5.png"
output_image_path = "output_image.png"

# 调用函数进行转换
convert_black_to_white(input_image_path, output_image_path)
