"""
超市找零小程序
"""
# 1,录入商品价格,录入商品数量,录入顾客付款金额
unit_price=input("所购商品价格:")
num=input("所购商品数量:")
total_price=float(unit_price)*float(num)

# 2,计算余额
money=input('顾客付款金额:')
change=float(money)-total_price
# 3,打印,应找零
if change>=0 :
    print('应找零:'+str(change))
else :
    print('你付的钱不够')