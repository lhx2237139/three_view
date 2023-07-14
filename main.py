import matplotlib.pyplot as plt
import numpy as np
import three
import gen_question

def gen_figure(cuboids,index):
    '''
    已知坐标（元组形式），生成具体的一张图片
    :param cuboids:
    :return:
    '''
    ax = fig1.add_subplot(111, projection='3d')
    # 绘制立方体
    for position in cuboids:
        ax.bar3d(*position, 1, 1, 1,color='white', edgecolor='black')

    # 设置坐标轴标签
    # ax.set_xlabel('X')
    # ax.set_ylabel('Y')
    # ax.set_zlabel('Z')
    ax.view_init(elev=8, azim=-85)

    ax.axis('off')
    ax.set_xlim(0, 5)
    ax.set_ylim(0, 2)
    ax.set_zlim(0, 4)
    # 显示图形
    #plt.show()
    plt.savefig(r'./picture/'+str(index)+'.png')

def axis_gen(Y,X,row):
    '''
    已知x,y,z具体信息，生成对应的坐标信息
    :param Z:
    :param X:
    :return:
    '''

    cube = []
    # 生成具体的一张图片
    for y in range(Y):
        for x in range(X):
            for z in range(row[y][x]):
                pos = (x,y,z)
                cube.append(pos)
    return cube

if __name__ == '__main__':
    import itertools
    # 批量生成图片
    # 定义列表大小
    rows = 3
    cols = 3
    a = [0,1,2,3]
    # 生成3*3=9个数的排列组合
    combinations = list(itertools.product(a,a,a,a,a,a,a,a,a))

    # 输出结果
    for index,row in enumerate(combinations):
        # 清除figure对象
        plt.cla()
        plt.close("all")

        if sum(row)<4 or sum(row)>6:
            continue

        row1 = row[:3]
        row2 = row[3:6]
        row3 = row[6:]

        pic_row = [row1,row2,row3]
        cube = axis_gen(3,3,pic_row)

        # 生成图片的同时保存图片
        fig1 = plt.figure(dpi=400, figsize=(4, 4))
        gen_figure(cube,index)
        #plt.show()
        # 生成对应的答案并保存图片
        fig,numbers = three.answer(pic_row,index)
        #plt.show()

        # 将两幅图融合成一道题目并保存在对应的答案文件夹中 'merge/A B C D'
        gen_question.merge(index,numbers)

        xxx = '调试'




