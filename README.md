# 三视图题目自动生成

## 环境
- numpy
- matplotlib
- random
- pillow

## 文件结构
- main.py 
  - 主文件
  - 直接运行即可得到对应题目
  - 目前参数对应的是生成3*3*3立方体的组合，其中块数为4~6块的组合
  - 调用gen_figure(cube,index)，生成立方体并保存在`picture`文件夹内

- three.py
  - 主文件调用文件，调用方法：`three.answer(pic_row,index)`
  - 生成对应的三视图和干扰选项，4个答案顺序不固定，将图片文件保存在`answer`文件夹中，并返回题目顺序值

- gen_question.py
  - 主文件调用函数，调用方法：`gen_question.merge(index,numbers)`
  - 将保存的立体图和对应的题目合并到一张图内，并随机生成对应正视图，俯视图，和侧视图的箭头
  - 将文件保存在`merge/A`对应的是答案为A的题目，`merge/B`，`merge/C`，`merge/D`同理

- row.py
  - 生成箭头的文件，在`gen_question.py`中调用,调用方法`row.row(merged_image,flag)`
  - 根据flag的值生成对应的三种箭头
