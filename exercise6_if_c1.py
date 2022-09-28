"""
在控制台获取一个月份
打印该月份天数,或者输入有误
"""
while True:
    month = int(input('请输入一个月份:'))
    if month < 1 or month > 12:
        print('输入有误')
    elif month == 2:
        print('本月有28天')
    elif month == 4 or month == 9 or month == 6 or month == 11:
        print('本月有30天')
    else:
        print('本月有31天')
    if input('按q键退出')=='q':
        break
