"""
    @ 功能：day06作业（if、for、while、for、函数）
    @ author：古城
    @ create：20200426 06:00
"""
import random

"""1. 你的微信好友当中有 5 个推销的，他们存在一个列表 black_list=['卖茶叶', '卖面膜', '卖保险', '卖花生', '卖手机']
当中, 请依次把这 5 个人分别从 black_list 当中删除，最后 black_list 为空。（不要使用 clear）
"""
# 1. 依次→循环，依次删除→.pop(固定index)
black_list = ['卖茶叶', '卖面膜', '卖保险', '卖花生', '卖手机']
while True:
    black_list.pop(0)
    if len(black_list) == 0:
        print("1. 现在black_list为空：{}".format(black_list))
        break

"""2. 使用遍历循环完成剪刀石头布游戏，提示用户输入要出的拳 ：石头（1）／剪刀（2）／布（3）/退出（4）
电脑随机出拳比较胜负，显示用户胜、负还是平局。运行如下图所示：
5d405338d8f29.png?OSSAccessKeyId=LTAItfPkNIKJFibY&Expires=4718096696&Signature=67Z%2BnH3xoSmCtY7QFd8G2CzQ4Zo%3D
提示：电脑随机出拳
使用随机数，首先需要导入随机数的模块 —— “工具包”
import random
导入模块后，可以直接在 模块名称 后面敲一个"."然后按 Tab键，会提示该模块中包含的所有函数
random.randint(a, b)，返回[a, b]之间的整数，包含a和b
random.randint(1, 10)  # 生成的随机数n: 1 <= n <= 10  
random.randint(4, 4)  # 结果永远是 4
random.randint(25, 12)  # 该语句是错误的，下限必须小于上限
"""
# 2. 写一个函数，作为用户出拳行为；写一个函数，作为系统随机出拳；用流程控制语言控制游戏进程

punch_list = {1: "石头", 2: "剪刀", 3: "布", 4: "退出"}
player_punch = None
pc_punch = None


def player_action():
    global player_punch
    try:
        player_punch = int(input("请按下面提示出拳：\n石头【1】 剪刀【2】 布【3】 退出【4】\n请输入你的选项："))
        if player_punch != 4:
            print("你的出拳为：{}，".format(punch_list[player_punch]), end="")
    except (KeyError, ValueError):
        print("输入错误")


def pc_action():
    global pc_punch, player_punch
    if player_punch in (1, 2, 3):
        pc_punch = random.randint(1, 3)
        print("电脑出拳：{}，".format(punch_list[pc_punch]),end="")


def judge():
    # 玩家：1 2 3
    # 电脑：2 3 1
    # 玩家胜：player_punch - pc punch in (-1,2)
    # 电脑胜：player_punch - pc_punch in (-2,1)
    # 平局：其他
    global pc_punch, player_punch
    if player_punch in (1, 2, 3):
        if player_punch - pc_punch in (-1, 2):
            print("你胜利了")
        elif player_punch - pc_punch in (-2, 1):
            print("你输了")
        else:
            print("平局")


print("2. 猜拳游戏：")
print("---石头剪刀布游戏开始---")
while True:
    player_action()
    pc_action()
    judge()
    if player_punch == 4:
        print("游戏结束")
        break

"""3. 编写如下程序
a.用户输入1-7七个数字，分别代表周一到周日
b.如果输入1~5，打印对应的“周一”~“周五”，如果输入的数字是6或7，打印输出“周末”
c.如果输入0，退出循环
d.输入其他内容，提示：“输入有误，请重新输入！”
提示：本题可以使用if和while循环，同时需要校验用户的输入是否正确。不用考虑浮点数等情况。
"""
print("3. 输入数字显示星期数")
weekday_list = {1: "星期一", 2: "星期二", 3: "星期三", 4: "星期四", 5: "星期五", 6: "周末", 7: "周末"}


def print_day():
    try:
        daytime = int(input("请输入代表星期天数的数字："))
    except ValueError:
        print("    输入有误，请重新输入")
        return "isNaN"
    if daytime == 0:
        return 0
    elif daytime < 8:
        print("    {}".format(weekday_list[daytime]))
    else:
        print("    输入有误，请重新输入")


while True:
    circle = print_day()
    if circle == 0:
        break

"""4. 选做：（不要求提交，面试之前背熟）
使用循环实现排序算法（冒泡，选择等算法选择一个，请自行了解。）
提示：利用for循环，完成a=[1,7,4,89,34,2]的排序（小的数字排前面，大的排后面），不能使用sort、sorted等内置函数或方法
"""
print("4. 冒泡排序：")
a = [1, 7, 4, 89, 34, 2]
for c1 in range(1, len(a)):
    for c2 in range(0, len(a) - c1):
        if a[c2] > a[c2 + 1]:
            a[c2], a[c2 + 1] = a[c2 + 1], a[c2]
print(a)
