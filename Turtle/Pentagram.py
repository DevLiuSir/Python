
# 导入模块并指定别名
import turtle as t
import time


# ****** 绘制五角星 ********


'''

   内角和公式： x = 180 * (n - 2); 公式描述：公式中n为多边形的边数。

   连接5个顶点得到一个正5边形
   由内角和公式：可知 每个角度数为 180 * (5 - 2) / 5 = 108 度

   180 - (180 - 108) * 2 = 36
   '''

# 五边形度每个角度
pentagon_degress = 180 * (5 - 2) / 5

# 五角星的内角: 36度
inner_degree = 180 - (180 - pentagon_degress) * 2

# 五角星的每个角度数
degree = 180 - inner_degree

t.title('绘制五角星')
t.pensize(5)
t.pencolor("yellow")
t.fillcolor("red")
t.begin_fill()

for _ in range(5):  # 循环5次画线
    t.forward(200)
    t.right(degree)

t.end_fill()

# 推迟 2秒执行
time.sleep(2)

# 文字
t.penup()
t.goto(-150, -120)
t.color("violet")
t.write("Done", font = ('Arial', 40, 'normal'))

# 启动事件循环，必须是乌龟图形程序中的最后一个语句
# 如果没有这个语句，代码运行完成后，窗口直接消失。
t.done()