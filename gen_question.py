from PIL import Image
import row
import random

def merge(index,number):
    # 打开两张PNG图片
    image1 = Image.open('picture/'+str(index)+'.png')
    image2 = Image.open('answer/'+str(index)+'.png')

    # 如果两张图片的尺寸不一样，可以调整其中一张图片的尺寸以匹配另一张图片
    if image1.size[0] != image2.size[0]:
        image2 = image2.resize((image1.size[0], image2.size[1]))

    image1 = image1.crop((0, 400, 1600, 1200))
    # 创建一个新的空白图片，宽度为两张图片之间的最大宽度，高度为两张图片的高度之和
    merged_image = Image.new('RGB', (max(image1.size[0], image2.size[0]), image1.size[1] + image2.size[1]))

    # 将两张图片粘贴到新的空白图片上
    merged_image.paste(image1, (0, 0))
    merged_image.paste(image2, (0, image1.size[1]))

    flag = random.randint(1,3)
    merged_image = row.row(merged_image,flag)
    # 保存合并后的图片
    answer_index = number[flag-1]-1
    file_list = ["A","B","C","D"]

    merged_image.save('merge/'+file_list[answer_index]+'/'+str(index)+'.png')

    return merged_image
