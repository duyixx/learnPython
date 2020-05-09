"""
    @ 功能：day09作业（文件操作）
    @ author：古城
    @ create：20200509 13:00
"""
import keyword, textwrap

# 简答题
# 1、什么是全局变量？
"""在一个.py文件最顶层创建的引用，讲座全局变量。
全局变量通常是相对于函数内部直接定义的作用域仅限于函数内的变量而言的
特点是在全局都会生效，与局部变量同名时在局部变量作用域内会被局部变量覆盖"""
# 2、什么是局部变量？
"""在函数内创建的引用，作用域为函数内部，用于实现函数的运算
使用global修饰的函数内变量可以在函数调用时作为全局变量生效"""
# 3、函数内部如何修改全局变量（如何声明全局变量 ）？
"""使用global"""
# 4、写出已经学过的所有python关键字，分别写出用途？
print(textwrap.fill('所有关键字：%s' % keyword.kwlist, width=100), end='\n' * 2)
已学过的关键字 = ['False', 'None', 'True', 'and', 'as', 'break', 'class', 'continue', 'def', \
           'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', \
           'import', 'in', 'is', 'lambda', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with']
未学过的关键字 = ['nonlocal', 'await', 'async', 'assert', 'yield']
print(textwrap.fill('已学过的关键字：%s' % 已学过的关键字, width=100), end='\n' * 2)
print(textwrap.fill('未学过的关键字：%s' % 未学过的关键字, width=100), end='\n' * 2)

# 5、简答题
# 写出你接触过的内置函数，并说明他们的作用。
"""input()  接收输入值，返回字符串
print()  输出
open()   打开/创建文件
enumerate() 生成二元素元组的列表
str()、int()、float()、bool()、tuple()、list()、dict()、set() 数据类型转换
sum() 合计、abs() 绝对值、max()、排序的最大值、min() 排序的最小值 、round() 四舍五入
super()  用以引用父类对象
len() 取长度
type() 返回数据的数据类型
format()  {}占位符的格式化输出
range()  python2：生成列表；Python3：生成可迭代对象
zip()  打包为二元素元组的列表
hash() 返回对象的hash值  id()    返回对象的内存地址
hex() otc()  返回十进制数的十六进制数、八进制数
"""
# 6、编写如下程序
# 有以下数据来自于一个嵌套字典的列表（可自定义这个列表），例如：
# person_info = [{"name": "yuze", "age": 18, "gender": "男", "hobby": "假正经", "motto": "I am yours"}, ....]
# 创建一个txt文本文件，来添加数据
# a.第一行添加如下内容： name, age, gender, hobby, motto
# b.从第二行开始，每行添加具体用户信息，例如：
# yuze, 17, 男, 假正经, I am yours
# cainiao, 18, 女, 看书, Lemon is best!

person_info = [{"name": "yuze", "age": 18, "gender": "男", "hobby": "假正经", "motto": "I am yours"},
               {"name": "cainiao", "age": 18, "gender": "女", "hobby": "看书", "motto": "Lemon is best!"},
               ]


def cwrdata(dictlist_temp):
    """功能：把传入的字典型列表按指定形式写入文件person_data
    dictlist_temp：传入的列表
    """
    # 创建文件person_data，第一行写入列表字典元素的第一个元素的key
    with open('person_data', 'w+', 1, encoding='utf-8') as file:
        line_head_original = str(list(dictlist_temp[0].keys()))
        line_head = line_head_original.replace("'", "").replace("[", "").replace("]", "")
        file.writelines(line_head + '\n')
        # file.flush()
        # file.seek(0, 0)
        # print(file.readline())
        # file.close()
        # 添加用户信息
        for i in range(0, len(dictlist_temp)):
            line_info_original = str(list(dictlist_temp[i].values()))
            line_info = line_info_original.replace("'", "").replace("[", "").replace("]", "")
            file.write(line_info + '\n')
        file.close()


def redata(dictlist_temp):
    """读取cwrdata()通过dictlist_temp生成的文件
    """
    cwrdata(dictlist_temp)
    with open('person_data', 'r', encoding='utf-8') as reader:
        lines = reader.read()
        print(lines)


redata(person_info)

# 6、编写如下程序
# 有两行数据，存放在txt文件里面(手动建立文件，并添加如下数据)：
# url:/futureloan/mvc/api/member/register@mobile:18866668888@pwd:123456
# url:/futureloan/mvc/api/member/recharge@mobile:18866668888@amount:1000
# 请利用上课所学知识，把txt里面的两行内容，取出然后返回如下格式的数据：（可定义函数）
# [{'url':'/futureloan/mvc/api/member/register','mobile':'18866668888','pwd':'123456'},{'url':'/futureloan/mvc/api/member/recharge','mobile':'18866668888','amount':'1000'}]

# 创建文件url.txt，并写入数据
with open('url.txt', 'w+', encoding='utf-8') as prepare:
    prepare.writelines(
        "url:/futureloan/mvc/api/member/register@mobile:18866668888@pwd:123456\nurl:/futureloan/mvc/api/member/recharge@mobile:18866668888@amount:1000")
    prepare.close()


def get_data(file_path):
    "功能：从文件file_path中读取指定格式的文件输出为[{},{}]格式的字典型列表"
    result = []
    with open(file_path, 'r', encoding='utf-8') as reader:
        while True:  # 循环读取每一行的数据
            line_original = reader.readline()
            if line_original =="":  # 每次读取一行数据，如果读取的结果为空，则结束循环
                break
            else:  # 把第一行的数据转化为字典形式，并加入result列表
                line = line_original.replace('\n', '')
                line_list = line.split('@')
                dict_tem = {}
                for item in line_list:
                    item_list = item.split(':')
                    dict_tem[item_list[0]] = item_list[1]
                result.append(dict_tem)

    print(result)


get_data('url.txt')
