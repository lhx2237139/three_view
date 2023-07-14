from PIL import Image, ImageDraw

def row(image,flag):
    draw = ImageDraw.Draw(image)

    # 箭头起始和结束位置的坐标
    if flag == 1:
        # 正视图
        start_x, start_y = 750, 750
        end_x, end_y = 800, 650
    elif flag == 2:
        # 侧视图
        start_x, start_y = 350, 400
        end_x, end_y = 450, 400
    else:
        # 俯视图
        start_x, start_y = 800, 20
        end_x, end_y = 800, 100

    # 设置箭头颜色为红色
    arrow_color = (255, 0, 0)

    # 绘制直线
    draw.line((start_x, start_y, end_x, end_y), fill=arrow_color, width=5)

    # 绘制箭头头部
    head_length = 20
    head_width = 10

    dx = end_x - start_x
    dy = end_y - start_y

    #angle = -30  # 可根据需要调整箭头的倾斜角度

    # 计算箭头头部三个点的坐标
    point1 = (end_x + int(head_length * dx / ((dx**2 + dy**2)**0.5)),
              end_y + int(head_length * dy / ((dx**2 + dy**2)**0.5)))
    point2 = (end_x + int(head_width * dy / ((dx**2 + dy**2)**0.5)),
              end_y - int(head_width * dx / ((dx**2 + dy**2)**0.5)))
    point3 = (end_x - int(head_width * dy / ((dx**2 + dy**2)**0.5)),
              end_y + int(head_width * dx / ((dx**2 + dy**2)**0.5)))

    head_points = [point1, point2, point3]

    draw.polygon(head_points, fill=arrow_color)

    return image