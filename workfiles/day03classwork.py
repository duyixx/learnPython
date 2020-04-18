"""
    @ 功能：第三天作业和笔记
    @ author：古城
    @ create：20200418 22:00
"""


# 课程笔记：
# 3.1字符串：str
"""
拼接：+    ,   sep.join(iterable)
重复：*
转义：  续行\   换行\n    空\0   制表\t    换页\f
不转义：r'str'
"""
# 3.1a 格式化输出
"""
    使用{}： 
    模板：{[index]:[:[[fill]align][sign][#][width][.precision][type]]}
        如：{1:@>6.1f}   表示空补@，位宽6，保留一位小数右对齐的浮点数   
          template = "索引为1、右对齐6.1：{1:@>6.1f}"
    调用：print(template.format(元素1,元素2,元素3))
    特点：每个占位符{}都必须有元素对应: 输入元素数>=占位符数
    type： s  字符串、d 十进制整数、f 浮点数 、e 以科学计数法表示
"""
# template = "索引为1、右对齐6.1：{1:@>6.1f}"
# print(template.format(10.11,20.22,30.33))   # 索引为1、右对齐6.1：@@20.2

"""使用%
    模板：%[-][+][0][m][.n]格式化字符    
        如：template = "十进制整数：%09d\t   字符串：%s \t  浮点数：%f"
        %s：字符串（str()）    %c：单个字符    %d：十进制整数    %f：浮点数  %%：百分号
    调用：print(template%(元素A,元素B,元素C,))
    特点：位宽m包括小数点， 输入元素数==占位符数
"""
# print("学号%d的同学是%s，有%07.3f红魔石"%(10086,"但丁",123))
#
# # 3.1b 字符串常用方法
# str31 = 'hello python1 hahaha  *\n'
    # .find() :检索是否包含指定字符串，有则返回第一个的首字符的索引，否则返回-1    str.find("sep")
    # .index() 同.find()，但要查找的内容不存在时会抛出异常，
    # .rindex()，同.index()，但从右边开始查找
# print(str31.find('ha',17))
    # .count() 返回指定字符串在目标字符串中出现的次数   str.count('sub'[,start[,end]])
    # .replace()改变某个字符后返回，默认全改变（原变量不变,也不能通过切片改变）
# print(str31.count('h')-str31.count('o',7))
# print(str31.replace('h','k'))
# print(str31)
    # 操作元素返回字符串
    # .split()以分隔符分割字符串，返回一个列表    str.split([sep[,maxsplit]])，
        #不指定分隔符sep时按空白符(' '、\n、\t)分割且连接在一起的空白符只分割一次；指定则遇到一次分割一次
        #maxsplit，最多分割次数
    # join()返回以分隔符分隔合并的字符串  sep.join(iterable)
# url = ','.join(['http://yuming/login','post',"参数1","参数2"])
# print(url)
# print(url.split(',',2))
# print(''.join(["555","aaa"]))
# print(range(1,10,3))
    # range() 返回的是一个可迭代对象
    # .strip()，去掉首尾的指定符号，不指定则去掉空白符，指定则去掉指定字符串   str.strip("sep")
        # 左侧？lstrip()，右侧？rstrip()
        #只能去掉首尾的字符。去掉全部的某个字符？用split()按字符分隔后再用""进行join()
# print("   空   格   ".strip())
# print("* 空*格*".strip('*'))
# print(str31.strip('\n'))
    #upper()、lower()，全大写、小写返回，swapcase()大小写互换
    #切片：截取字符串并返回str[start:end:step]
    #len()字符串长度
# print("str31长：",len(str31))
# print("全大写"+str31.upper())
    # isdigit()，只包含数字型字符则返回TRUE，否则Flase
    # islower()、isupper()
    # .startwith()、.endwith()，以关键字符开头、结尾则返回True，否则返回Flase
# print(str31.startswith('e'))
# print(str31.startswith('e',1))
# print(str31.endswith('n'))
# print(str31.endswith('n',5,12))
# print(str31.isdigit())
# print('111'.isdigit())
    # .encode()字符串编码后返回（简中为gb2312）
        # str.encode([encoding='utf-8'][,errors='strict'])
            # encoding指定要转成的格式，errors指定错误处理方式：strict抛出异常、ignore忽略非法字符、replace用？代替非法字符
            # 默认为utf-8和strict,  b''表bytes对象
    # .decode()解码；解码采用的字符编码要和编码时一致
# remmf = 'rem是我老婆'
# remmf_engbk=remmf.encode(encoding='gbk',errors='replace')
# print('编码：',remmf_engbk)
# remmf_degbk=remmf_engbk.decode(encoding='gbk',errors='replace')
# print('解码：',remmf_degbk)
# print('不同编码规则：',remmf_engbk.decode(encoding='utf-8',errors='replace'))  #不同编码规则
#         #ps：python中字符串str有两种形式：
            # Unicode字符（ASCII或其他，在内存中显示为unicode字符：rem是我老婆）
            # bytes（二进制数据，在网络传输和磁盘储存用bytes类型： b'rem\xca\xc7\xce\xd2\xc0\xcf\xc6\xc5'）

# 3.2 列表list
''' 1：空列表,长度0'''
# t1 = []
# print(type(t1))
# print(len(t1))
''' 2：一元素列表不用在后面加上逗号'''
# t2 = [1]
# print(type(t2))
# print(len(t2))
''' 3：列表元素可以是任意数据类型'''
# t3 = [1,0.0002,'str',True,(1,),[2,],{'key1':'15'},{'set1','set2'}]
# print(type(t3))
# print(len(t3))
''' 4 列表的操作：特性：有序可变（有序：有索引号；可变：元素值可增删改）'''
t4 = [1,0,0.0002,'str',True,True,False,(1,),[2,'asd'],{'key1':'15'},{'set1','set2'}]
''' ##  访问元素：索引和切片'''
# print(t4[-2].get('key1')[1])      #嵌套取值
# print(t4[2:7:2])                   #切片tuple[start:end:step]
# print(t4[::-1])                    #倒序输出
''' ## 增加元素.append(元素)  .insert(index,元素)   .extend(iterable)   加号'''
# t4.append('+1')             #每次调用在尾部增加且只能增加一个元素
# t4.insert(2,'insert')       #指定位置插入，其他元素后挪
# t4.extend(('a','b','c'))    #后接合并列表
# t4=[1,2,3] + t4             #连接号合并列表
# t4[-7].append('efg')
# print(t4)
''' ## 修改元素:用赋值语句'''
# t4[1] = 'alpha'
# print(t4)
''' ## 删除元素.pop(index)  .clear()    .remove(value)'''
# t4.pop(1)                       #删除指定索引的元素，不指定则删除最后一个
# t4.clear()                      #清空列表
# t4.remove(0)
# print(t4)
# print(t4.clear())
# print(t4.pop(-1))                 #注意：str.pop(index) 会删除str中指定索引的位置的字符，同时会返回被删除的value
                                    #而.clear()、.remove(value)  等往往返回是None
''' ## 其它用法：'''
    ## 获取元素的索引值.index(元素)、.count(元素)
# print(t4.index(0.0002))     # 结果：2      确定元素所在索引位置
# print(t4.count(1))          # 结果是：3：把1当做True来计数了   统计列表里该元素的个数
# print(t4.count(0))          # 结果是：2：把0当做False来计数了


# 作业
"""
1、.删除如下列表中的"矮穷丑"，写出 2 种或以上方法：
    info = ["yuze", 18, "男", "矮穷丑", ["高", "富", "帅"], True, None, "狼的眼睛是啥样的"]
2、现在有一个列表 li2=[1，2，3，4，5]，
    请通过相关的操作改成li2 = [0，1，2，3，66，4，5，11，22，33]，
    请写出删除列表中元素的方法，并说明每个方法的作用
3、有5道小题（使用列表操作完成）：
    a.  某相亲节目需要获取你的个人信息，请存储你的：姓名、性别、年龄
    b. 有一个人对你很感兴趣，平台需要您补足您的身高和联系方式；
    c, 平台为了保护你的隐私，需要你删除你的联系方式；
    d, 你为了取得更好的成绩，需要取一个花名，并修改自己的身高和其他你觉得需要改的信息。
    e, 你进一步添加自己的兴趣，至少需要 3 项。
"""
"""回答："""
    # 1.
info = ["yuze", 18, "男", "矮穷丑", ["高", "富", "帅"], True, None, "狼的眼睛是啥样的"]
# info.pop(info.index("矮穷丑"))
# info.remove("矮穷丑")
# print(info)
    # 2.
li2 = [1,2,3,4,5]
        # 通过重新赋值
# li2 = [0,1,2,3,66,4,5,11,22,33]
        # 使用 .append() .insert() .extend()
# li2.insert(0,0)
# li2.insert(4,66)
# li2.append(11)
# li2.extend([22,33])
# print(li2)
    # 3.
li = []
# a  li = [姓名，性别，年龄，]
li = ["姓名：刘德华", "性别男", 18]
# b 身高199  电话10086
he = "身高：199"
pn = "电话：10086"
li = li +[he, pn]
# c
li.remove("电话：10086")
# d 花名 身高200
li.append("花名：帅过梁朝伟")
li[3]="身高200"
# e
li.extend(["抓小偷", "当卧底", "三年又三年"])

print(li)
