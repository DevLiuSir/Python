
import turtle
import time


# ******** 绘制太阳花 *********


turtle.title('太阳花')
turtle.screensize(500, 500, "white")   # 设置画布大小
turtle.showturtle()         # 显示箭头
turtle.speed(10)            # 设置画笔移动速度,画笔绘制的速度范围[0,10]整数, 数字越大越快
turtle.begin_fill()         # 图形准备开始填充
turtle.color('red', 'yellow') # color(): 参数1: 画笔色, 参数2: 填充色

for _ in range(50):         # 循环50次
    turtle.forward(200)     # 向当前画笔方向移动 200 像素长度
    turtle.left(170)        # 逆时针移动 170°

turtle.end_fill()           # 填充完成

# 启动事件循环 -调用Tkinter的mainloop函数。必须是乌龟图形程序中的最后一个语句。
turtle.done()