"""
在控制台中录入一个成绩
判断(优秀/良好/及格/不及格/输入有误)
"""
score = float(input('请输入成绩:'))
if score > 100 or score < 0:
    print('输入有误')
elif score >= 90:
    print('成绩优秀')
elif score >= 80:
    print('成绩良好')
elif score >= 60:
    print('成绩及格')
elif score > 0:
    print('成绩不及格')
