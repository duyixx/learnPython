"""
    @ 功能：day05作业（tuple、dict、set）
    @ author：古城
    @ create：20200423 23:00
"""


# 1、一家商场在降价促销，所有原价都是整数（不需要考虑浮点情况），如果购买金额50-100元(包含50元和100元)之间，会给10%的折扣，
# 如果购买金额大于100元会给20%折扣。编写一程序，询问购买价格，再显示出折扣（%10或20%）和最终价格。
price = int(input("1. 判断折扣和折扣后价格：\n请输入原价:"))
if price < 50:
    print("没有达到优惠金额，应付{:.2f}元".format(price))
elif price <= 100:
    print("价格间于50-100元，折扣10%，应付{:.2f}元".format(price*0.9))
else:
    print("价格大于100元,折扣20%，应付{:.2f}元".format(price*0.8))


# 2 判断是否为闰年
# 提示:
# 输入一个有效的年份（如：2019），判断是否为闰年（不需要考虑非数字的情况）
# 如果是闰年，则打印“2019年是闰年”；否则打印“2019年不是闰年”
# 什么是闰年，请自行了解（需求文档没有解释）
year = int(input("2. 请输入年份:"))
print(str(year)+"年是闰年" if (year%4 == 0 and year%100 != 0)or year%400 ==0 else str(year)+"年不是闰年" )


# 3.求三个整数中的最大值    提示：定义 3 个变量
num1 = float(input("3. 判断三个数中的最大值：\n请输入三个数"))
num2 = float(input())
num3 = float(input())
# 3.1使用max()
print(num1, num2, num3,"中最大的是", max(num1, num2, num3))
# 3.2if
if num1>=num2 and num1>=num3:
    print("三个数中最大的是", num1)
elif num2>=num3:
    print("三个数中最大的是", num2)
else:
    print("三个数中最大的是", num3)


# 4，  使用for打印九九乘法表    提示：输出九九乘法表，格式如下：（每项数据之间空一个Tab键，可以使用"\t"）
print("4. 输出九九乘法表：")
for x in range(1,10):
    for y in range(1,x+1):
        print(y, "*", x, "=", x*y, end="\t")
    print("")
