"""
在控制台录入一个数字
再录入一个运算符(+,-,*,/),最后再录入一个数字
根据运算符计算2个数字
如果运算符不是加减乘除,提示运算符有误
"""
number1 = float(input('请录入一个数字:'))
yunsuanfu = input('请录入运算符:')
number2 = float(input('请再次录入一个数字:'))
if yunsuanfu == '+':
    print(number1 + number2)
elif yunsuanfu == '-':
    print(number1 - number2)
elif yunsuanfu == '*':
    print(number1 * number2)
elif yunsuanfu == '/':
    print(number1 / number2)
else:
    print('运算符输入有误')
