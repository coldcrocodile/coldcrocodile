"""
根据成绩判断等级,如果录入空字符串则退出程序
如果程序录入错误达3次,则退出成绩,并提示"成绩错误过多"
"""
# count = 0
# while count < 3:
#     str_score = input('请输入成绩:')
#     if str_score=='':
#         break
#     score = float(str_score)
#     if score > 100 or score < 0:
#         print('输入有误')
#         count += 1
#     elif score >= 90:
#         print('成绩优秀')
#     elif score >= 80:
#         print('成绩良好')
#     elif score >= 60:
#         print('成绩及格')
#     elif score > 0:
#         print('成绩不及格')
# else:
#     print('成绩输入错误太多')


import random

count = 0
count2=0
for item in range(5):
    random_number1 = random.randint(1, 21)
    random_number2 = random.randint(1, 21)
    print('%s+%s=?' % (str(random_number1), str(random_number2)))
    input_number = input('请输入答案:')
    if int(input_number) == random_number1 + random_number2:
        print('回答正确,加油')
        count += 10
        count2+=1
    else:
        print('回答错误')
print('共计答对%s题,得分为:%s分' %(count2,count))
