"""
录入一个年份
如果是闰年,给变量day赋值28
"""
year = int(input('请输入一个年份:'))
if year % 4 == 0 or year % 40 == 0:
    day = 29
else:
    day = 28
print(day)
