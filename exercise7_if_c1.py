"""
在控制台中获取一个整数
如果是偶数,为变量state赋值为偶数,否者为奇数
"""
number = int(input('请输入一个整数:'))
if number % 2 == 0:
    state = '偶数'
else:
    state = '奇数'
print(state)
