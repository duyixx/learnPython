"""
    @ 功能：day04作业（tuple、dict、set）
    @ author：古城
    @ create：20200422 22:00
"""


# 一、请指出下面那些为可变类型的数据，那些为不可变类型的数据
"""
首先必须明确“可变”是什么意思：
可变/不可变类型,指的是：内存id不变，type也不变的前提下，value是否是可变的。
对于不变对象来说，调用对象自身的任意方法不会改变对象自身的内容，但会创建新的对象并返回从而保证对象本身是不可变的。
如:  a = "abc"    a.replace("a","A")，a仍然是"abc"，说明"adc"字符串是不可变对象
s = [1, 2, 3]    s.append(4),这时s为[1, 2, 3, 4]，说明[1, 2, 3, 4]列表是可变对象
简要记忆：固有数据类型是不可变数据类型。list、set、dict是可变数据类型
"""
# 1、(11)
# type((11))为int，基本数据类型，不可变对象
# 2、{11，22}
set1 = {11, 22}
set1id1 = id(set1)
set1.add(33)
set1id2 = id(set1)
print("{11,22}数据类型是", "可变的" if set1id1 == set1id2 else "不可变的")
# type不变、id不变，set1的值由{11,22}变成了{11,22,33}, 所以是可变的
# 3、([11,22,33])
li1 = ([11, 22, 33])
l1id1 = id(li1)
li1.append(44)
l1id2 = id(li1)
print("([11, 22, 33])数据类型是", "可变的" if l1id1 == l1id2 else "不可变的")
# 这是单元素，实际上是list，所以对象的值是可变的
# 4、{"aa":111}
dict1 = {"aa": 111}
d1id = id(dict1)
dict1.pop("aa")
d2id = id(dict1)
print('{"aa":11}数据类型是', "可变的" if d1id == d2id else "不可变的")

# 也有一种说法是指将该对象赋值给变量时变量的内存地址会不会改变
# (11)  地址不变→不可变
aa = (11)
print("int1",id(aa))
aa = (11)
print("int1",id(aa))
# {11，22}  地址改变→可变
ss1 = {11,22}
print("set1:",id(ss1))
ss1 = {11, 22}
print("set2:",id(ss1))
# ([11, 22, 33])  可变
l1 = ([11, 22, 33])
print("list1:",id(l1))
l1 = ([11, 22, 33])
print("list2:",id(l1))
# {"aa":111} 可变
d1 = {"aa":111}
print("dict1:",id(d1))
d1 = {"aa":111}
print("dict2:",id(d1))

# 二、当前有一个列表 li = [11,22,33,22,22,44,55,77,88,99,11]，
#  要求一：去除列表中的重复元素，
#  要求二：删除 77，88，99这三个元素
li = [11,22,33,22,22,44,55,77,88,99,11]
    # 要求一：使用set
li = list(set(li))
print(li)
    # 要求二：使用.remove()
for tem in [77, 88, 99]:
    while li.count(tem) > 0:
        li.remove(tem)
        continue
print(li)
# 三、有下面几个数据，
# t1 = ("aa",11)      t2= (''bb'',22)    li01 = [("cc",11)]
# 请通过学过的知识点，进行相关操作变为如下字典: {"aa":11,"cc":11,"bb":22}
t1 = ("aa",11)
t2 = ("bb", 22)
li01 = [("cc",11)]
# 使用多个二元元组构建字典
dict2 = dict((t1, li01[0], t2))
print(dict2)

# 四，将上个作业的相亲节目用字典实现
# a. 某相亲节目需要获取你的个人信息，请存储你的：姓名、性别、年龄
# b. 有一个人对你很感兴趣，平台需要您补足您的身高和联系方式；
# c, 平台为了保护你的隐私，需要你删除你的联系方式；
# d, 你为了取得更好的成绩，需要取一个花名，并修改自己的身高和其他你觉得需要改的信息。
# e, 你进一步添加自己的兴趣，至少需要 3 项。
# 创建个人信息字典info
info = dict.fromkeys(["姓名", "性别", "年龄", "身高", "联系方式", "花名", "兴趣"])
# a.使用赋值
info["姓名"] = "柠檬梁朝伟"
info["性别"] = "男"
info["年龄"] = 17
print(info)
# b
info["身高"] = "188m"
info["联系方式"] = 110
print(info)
# c 使用del
info.pop("联系方式")
print(info)
# d
info["花名"] = "我是警察"
# e 兴趣的值有三个，用list
info["兴趣"] = ["唱", "跳", "~rap~"]
print(info)

