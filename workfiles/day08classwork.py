"""
    @ 功能：day07作业（函数）
    @ author：古城
    @ create：20200501 01:00
"""
import random

# 1. 定义一个函数，传入一个字典和字符串，判断字符串是否为字典中的值，
# 如果字符串不在字典中，则添加到字典中，并返回新的字典
print("   1.")
def funcif(var1, var2):
    '''功能：判断传入第一个参数为字典、第二个参数为字符串时返回var_ok，否则返回0
    '''
    if type(var1) == type(dict()) and type(var2) == type(str()):  # type(str) → type，type(str()) → str
        return "var_ok"
    else:
        return 0


def in_dict_value(dictin, strin):
    '''功能：判断输入的第二个参数是否为第一个参数中的值
        dictin：只能传入字典类型
        strin：只能传入字符串类型
        stage:记录传入参数是否符合要求，0为不符合，"var_ok"为符合
    '''
    stage = funcif(dictin, strin)
    dictold = dictin
    dictnew = dictin
    if strin not in dictold.values() and stage == "var_ok":
        k = "key"
        while True:
            if k not in dictold.keys():
                dictnew[k] = strin
                break
            else:
                k = k + str(random.random.__hash__())
        return dictnew
    elif stage == 0:
        # raise ValueError("函数传参不符合要求")           # raise ExceptionName(reasion)
        print("函数传参错误")
    else:
        return "字符串在字典值内"


print(in_dict_value({"key": "value", "b": 2, "c": 3, "d": 1, "e": 4}, ["sdfsdf", ]))


# 2. 通过定义一个计算器函数，调用函数传递两个参数，然后提示选择【1】加 【2】减【3】乘 【4】除 操作，选择之后返回对应操作的值。
print("   2.")

def slim_clac(var1, var2):
    if type(var1) in (type(int()), type(float())) and type(var2) in (type(int()), type(float())):
        operator_index = input("请选择计算方法：\n       【1】加 【2】减【3】乘 【4】除")
        if operator_index == "1":
            return var1 + var2
        if operator_index == "2":
            return var1 - var2
        if operator_index == "3":
            return var1 * var2
        if operator_index == "4":
            try:
                return var1 / var2
            except ZeroDivisionError:
                print("你体育老师教你的除数可以为零吗？  @.@ #!!")
        if operator_index not in ("1", "2", "3", "4"):
            return "传入参数有误"
    else:
        return "传入参数有误"


print(slim_clac(10086, 0))


# 3. 一个足球队在寻找年龄在15岁到22岁的女孩做拉拉队员（包括15岁和22岁）加入。
# 编写一个程序，询问用户的性别和年龄，然后显示一条消息指出这个人是否可以加入球队，询问10次后，输出满足条件的总人数。
print("   3.")

def query():
    count = 0
    for step in range(10, 0, -1):
        gender = input("第{}个小朋友，你是gg还是mm啊？（>.<）".format(11 - step))
        if gender not in ("gg", "mm"):
            print("要用'gg'和'mm'回答，下一个")
            continue
        try:
            age = int(input("今年多大了呀？（O(∩_∩)O~）"))
            if (22 > age > 15) and gender == "mm":
                count += 1
        except TypeError:
            print("要正确告诉我你的年龄，下一个")
            continue
    print("满足条件的有{}个".format(count))


query()

# 4. 数据转换
# 有一组用例数据如下：
cases = [
    ['case_id', 'case_title', 'url', 'data', 'excepted'],
    [1, '用例1', 'www.baudi.com', '001', 'ok'],
    [4, '用例4', 'www.baudi.com', '002', 'ok'],
    [2, '用例2', 'www.baudi.com', '002', 'ok'],
    [3, '用例3', 'www.baudi.com', '002', 'ok'],
    [5, '用例5', 'www.baudi.com', '002', 'ok'],
]
# 要求一：把上述数据转换为以下格式
res1 = [
    {'case_id': 1, 'case_title': '用例1', 'url': 'www.baudi.com', 'data': '001', 'excepted': 'ok'},
    {'case_id': 4, 'case_title': '用例4', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'},
    {'case_id': 2, 'case_title': '用例2', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'},
    {'case_id': 3, 'case_title': '用例3', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'},
    {'case_id': 5, 'case_title': '用例5', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'}
]
# 要求二：把上面转换好的数据中case_id大于3的用例数据获取出来,得到如下结果
res = [
    {'case_id': 4, 'case_title': '用例4', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'},
    {'case_id': 5, 'case_title': '用例5', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'}
]
cases = [
    ['case_id', 'case_title', 'url', 'data', 'excepted'],
    [1, '用例1', 'www.baudi.com', '001', 'ok'],
    [4, '用例4', 'www.baudi.com', '002', 'ok'],
    [2, '用例2', 'www.baudi.com', '002', 'ok'],
    [3, '用例3', 'www.baudi.com', '002', 'ok'],
    [5, '用例5', 'www.baudi.com', '002', 'ok'],
]


# 要求一：
# 分析： res1 = [dict0,dict1,dict2,dict3,dict4], dict2=dict(zip(casea[0],case[2]))
print(" 4. 要求一")

def translate1(cases6_5):
    res1 = list()
    for i in range(1, len(cases6_5)):
        res1.append(dict(zip(cases6_5[0], cases6_5[i])))
    return res1


for item in translate1(cases):
    print(item)

# 要求二：
# 分析：基于要求一，要使用translate1()； case_id 的定位：res1[i]["case_id"],要求>3； Python3.6以上dict有序；
# 获取用例数据：res1[i]
print("4. 要求二")

tem_list = translate1(cases)


def translate2(cases):
    res = list()
    for i in range(0, len(cases)):
        if cases[i]["case_id"] > 3:
            res.append(cases[i])
    return res


for item in translate2(translate1(cases)):
    print(item)

# 5. 画出函数相关内容的思维导图或者笔记
# ....