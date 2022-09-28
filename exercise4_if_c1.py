"""
在控制台中录入4个数字
打印最大的一个
"""
number1 = float(input('请输入第一个数字:'))
number2 = float(input('请输入第二个数字:'))
number3 = float(input('请输入第三个数字:'))
number4 = float(input('请输入第四个数字:'))
if number1 >= number2:
    if number1 >= number3:
        if number1 >= number4:
            print('最大的数字是' + str(number1))
        else:
            print('最大的数字是' + str(number4))
    elif number3 >= number4:
        print('最大的数字是' + str(number3))
elif number2 >= number3:
    if number2 >= number4:
        print('最大的数字是' + str(number2))
    else:
        print('最大的数字是' + str(number4))
elif number3 >= number4:
    print('最大的数字是' + str(number3))
else:
    print('最大的数字是' + str(number4))
