"""
计算秒数
"""
# 1,输入秒数,小时数,天数
minitues = int(input('请输入分钟数:'))
hours = int(input('请输入小时数:'))
days = int(input('请输入天数:'))
# 2,计算

total_seconds = minitues*60 + hours*60*60 + days*24*60*60
# 3,输出
print('总秒数为:'+str(total_seconds))