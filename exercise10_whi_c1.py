"""
控制台中随机产生一个数
让人猜测并且提示大小
"""
import random
random_number = random.randint(1, 100)
count = 0
while count<3:
    guess_number = int(input('请输入您猜的数字:'))
    count += 1
    if guess_number > random_number:
        print('大了')
    elif guess_number < random_number:
        print('小了')
    else:
        print('猜对了!您一共猜了' + str(count) + '次')
        break
else:
    print('游戏结束')