"""
    @ 功能：day07作业（函数）
    @ author：古城
    @ create：20200429 22:00
"""


# 1. 定义函数：将用户输入的所有数字相乘之后对20取余数，用户输入的数字个数不确定
def func1():
    '''函数用于将输入的数字相乘并对20取余。用户输入非数字时结束函数
        vartem:第一次输入
        var：再次输入
    '''
    print("__________第一题____________________\n请输入连乘的数字,不输入数字为退出")
    try:
        vartem = float(input())
        stro = str(vartem)
    except ValueError:
        return
    while True:
        print("{}除以20余{}".format(stro, vartem % 20))
        try:
            var = float(input("请输入要继续连乘的数字，不输入数字为退出！！"))
        except ValueError:
            break
        vartem = vartem * var
        stro += "*" + str(var)


func1()

# 2. 编写函数，检查传入列表的长度，如果大于2，那么仅仅保留前两个长度的内容，并将新内容返回
print("__________第二题____________________\n")


def func2(listtem):
    '''函数用于将传入列表长度大于2则返回前两个元素'''
    if len(listtem) > 2:
        return listtem[0:2:1]
    else:
        return "{}长度不足2".format(listtem)


print(func2([1, ]))

# 3.列表去重：定义一个函数 def remove_element(m_list):，将列表[10, 1, 2, 20, 10, 3, 2, 1, 15, 20, 44, 56, 3, 2, 1]去除重复元素
print("__________第三题____________________")
p_list = [10, 1, 2, 20, 10, 3, 2, 1, 15, 20, 44, 56, 3, 2, 1]


def remove_element(m_list):
    '''函数用于对列表去重；m_list为传入的列表'''
    global p_list
    p_list = list(set(m_list))


remove_element(p_list)
print(p_list)

# 4.编写如下程序
# 尝试函数封装：
# 输入一个人的身高(m)和体重(kg)，根据BMI公式（体重除以身高的平方）计算他的BMI指数
# a.例如：一个65公斤的人，身高是1.62m，则BMI为 :  65 / 1.62 ** 2 = 24.8
# b.根据BMI指数，给与相应提醒
# 低于18.5： 过轻 18.5-25：   正常 25-28：      过重 28-32：      肥胖 高于32：   严重肥胖
print("__________第四题____________________")


def func_bmi(height, weight):
    '''函数用于计算bmi指数并判断健康情况；height为身高（m），weight为体重（kg）'''
    bmi = weight / height ** 2
    result = {1: "过轻，娇柔细弱", 2: "正常", 3: "过重", 4: "肥胖", 5: "严重肥胖，你嫁不出去了"}
    if bmi < 18.5:
        index = 1
    elif bmi < 25:
        index = 2
    elif bmi < 28:
        index = 3
    elif bmi < 32:
        index = 4
    else:
        index = 5
    template = "身高:{:.2f}m\n体重：{:.2f}kg\nBMI指数为:{:.2f}，{}"
    print(template.format(height, weight, bmi, result[index]))


func_bmi(2.0, 200)

