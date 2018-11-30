import calendar

"""
def isleap(year)函数 : 闰年返回True，非闰年返回False
return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

"""

year = int(input("请输入一个年份: "))

check_year = calendar.isleap(year)

if check_year == True:
    print("%d是闰年" % year)
else:
    print("%d是平年" % year)
    