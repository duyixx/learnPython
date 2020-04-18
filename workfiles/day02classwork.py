# coding:utf8
"""
    @ 功能：第二天作业
    @ author：古城
    @ create：20200416 22:02
"""

"""
作业：
1、现在有字符串：str1 = 'python cainiao 666'
    1、请找出第 5 个字符。
    2、请复制一份字符串，保存为 str_two
    3、请找出最中间的字符。（字符串长度是偶数。）
    4,   选做：有基础的同学可以尝试字符串长度不确定的情况。(涉及到后面内容，不需要提交)
2、卖橘子的计算器：写一段代码，提示用户输入橘子的价格，和重量，最后计算出应该支付的金额！（不需要校验数据，都传入数字就可以了。）
3.演练字符串操作
    my_hobby = "Never stop learning!"
    截取从 位置2 ~ 位置6 的字符串
    截取从 位置2 ~ 末尾 的字符串
    截取从 开始位置~ 位置6 的字符串
    截取完整的字符串
    从 索引3 开始，每2个字符中取一个字符
    截取字符串末尾两个字符
    字符串的倒序
    说明：“位置”指的是字符所处的位置（比如位置1，指的是第一个字符“N”），“索引”指的是字符的索引值（比如索引0， 代表的是第一个字符“N”）
4， 总结本节课内容，画出思维导图或者笔记详情。（这节课非常重要，务必进行总结）
"""

# 答案：
# 1:
str1 = 'pythin cainiao 666'
print(str1+"第5个字符是"+str1[4])
str_two = str1
print(str1+"中间的字符是"+str1[int(len(str1)/2-1)]+str1[int(len(str1)/2)])
# str1 = '100860a'
# 奇数个字符：中间位置索引是(len()-1)/2；     偶数个字符：中间位置索引是len()/2-1、len()/2。
print(str1[int((len(str1) - 1)/2)] if len(str1)%2==1 else str1[int(len(str1)/2-1)]+str1[int(len(str1)/2)])


# 2:
def orange_calc():
    wt = float(input("计算橘子价格\n请输入重量："))
    pce = float(input("请输入单价："))
    print("应付：￥"+str(wt*pce))


orange_calc()


# 3:
my_hobby = "Never stop learning!"
print(my_hobby[1:6])
print(my_hobby[1:])
print(my_hobby[:6])
print(my_hobby[:])
print(my_hobby[3::2])
print(my_hobby[-2::1])
i = -1
while i >= -len(my_hobby):
    print(my_hobby[i], end="")
    i -= 1


# 4. 课堂内容总结：
# 算术运算符：+   -   *   /   %   **   //
    """
    除法返回float：
    幂运算5 ** 2
    整除5 // 2
    取余5 % 2
    """
# 赋值运算符：
    """
    =  +=   -=   /=   *=
    """
# 比较运算符:
    """
    > < >= <= == !=
    """
# 逻辑运算符：
    """
    and or not 
    """
# 成员运算：
    """
    in    not in 
    """
# 字符串：str = "python hello world"
    """
    切片：str[start:end:step]  str[2,5,1]→yh
    长度len()         eg. len(str)   
    """
