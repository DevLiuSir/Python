
# 猜数字，输入1-100，核对a的值
a = '91'
print("please input a int number in 1-100")
x = input()
if a != x:
    print("sorry you are wrong!\ninput again:")
    x = input()
else:
    print("you are right")
input()
