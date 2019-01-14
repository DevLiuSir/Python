
# 打印九九乘法表

# ------------for循环九九乘法表------------
for i in range(1, 10):
    for j in range(1, i + 1):
        print('{} * {} = {}\t'.format(j, i, i * j), end="")
    print('\n')


# ------------while循环九九乘法表-----------
i = 1
while i < 10:
    j = 1
    while j < i + 1:
        print(f'{j} * {i} = {i * j}\t', end='')
        j += 1
    print()     # print函数默认换行
    i += 1
