
# 对日历的操作

# 引入日历模块
import calendar

# 引入 datetime 模块
import datetime


# 输入一个年份、月份，生成日历，根据月份从而计算天数

yy = int(input("输入年份: "))
mm = int(input("输入月份: "))
print(calendar.month(yy, mm))

"""
monthrange(): 返回工作日（0-6~周一至周日）即：最后一天为周几。
              和 天数（28-31) 输入的月份有多少天; 接收年、月。
"""
mothRange = calendar.monthrange(yy, mm)
print("%d月份共有%d天, 工作日: %d" %(mm, mothRange[1], mothRange[0]))


# 获取昨天的日期

def getyesterday():
    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    yesterday = today - oneday

    return yesterday

print("昨天日期为: %s" %(getyesterday()))

