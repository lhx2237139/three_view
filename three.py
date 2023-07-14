'''
生成对应的三视图和干扰选项，4个答案顺序不固定，返回题目顺序值
'''
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import random

def draw_square(x_start, y_start, size):
    '''
    画一个正方形
    '''
    x = [x_start, x_start, x_start + size, x_start + size, x_start]
    y = [y_start, y_start + size, y_start + size, y_start, y_start]
    plt.plot(x, y,color='black',linewidth=5)

def draw_combination(squares):
    if type(squares) == list:
        '''
        送入希望画的正方形的块数
        :param squares: [2,3,4]
        :return:
        '''
        x_start = 0
        y_start = 0
        size = 1

        for count in squares:
            for _ in range(count):
                draw_square(x_start, y_start, size)
                y_start += size
            x_start += size
            y_start = 0

        plt.axis('equal')

    else:
        '''
        画俯视图
        '''
        size = 1
        for x in range(3):
            for y in range(3):
                if squares[x][y]:
                    draw_square(y,x,size)
        plt.axis('equal')

def gen_block(blocks):
    '''
    分别生成正视图，侧视图和俯视图需要的块数
    :param block1: [[0, 1, 2], [2, 3, 4], [1, 1, 0]]
    :return: [2,3,4],[],[],[]
    '''
    zheng = [max(blocks[:,0]),max(blocks[:,1]),max(blocks[:,2])]
    ce = [max(blocks[2]),max(blocks[1]),max(blocks[0])]
    fu = blocks!=0
    ganrao = np.random.randint(0,2,(3,3))

    return zheng,ce,fu,ganrao

def draw(fig,view,i):
    num = '14'+str(i)
    ax = fig.add_subplot(eval(num))
    draw_combination(view)
    ax.set_xlim(-0.2, 3.3)
    ax.set_ylim(-0.2, 3.3)
    plt.xticks([])
    plt.yticks([])
    #ax1.axis('off')
    ax.set_title(str(i),fontsize=32, fontweight='bold')

    return ax

def answer(blocks,index):
    fig = plt.figure(figsize=(16, 4),dpi=100)  # 设置图形大小
    # 立体图
    #blocks = np.array([[0, 0, 0], [2, 3, 2], [1, 1, 0]])
    blocks = np.array(blocks)
    zheng,ce,fu,ganrao = gen_block(blocks)

    # 打乱四个答案的顺序
    numbers = [1, 2, 3, 4]
    # 使用shuffle函数对列表进行乱序
    random.shuffle(numbers)

    ax1 = draw(fig,zheng,numbers[0])
    ax2 = draw(fig, ce, numbers[1])
    ax3 = draw(fig, fu, numbers[2])
    ax4 = draw(fig, ganrao, numbers[3])

    # 调整子图间距
    plt.subplots_adjust(wspace=0.15)

    plt.savefig(r'./answer/'+str(index)+'.png')
    return fig,numbers








