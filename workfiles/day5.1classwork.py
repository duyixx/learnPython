"""
    @ 功能：51作业
    @ author：古城
    @ create：20200422 01:00
"""

# 题目： 完成以下字符串操作练习：
# 1, 将字符串 "abcd" 转成大写,
# 2, 计算字符串 "cd" 在 字符串 "abcd"中出现的位置
# 3, 字符串 "a,b,c,d" ，请用逗号分割字符串
# 4, "{name}喜欢{fruit}".format(name="李雷") 执行会出错，请修改代码让其正确执行
# 5, string = "Python is good", 请将字符串里的Python替换成 python,并输出替换后的结果
# 6, 有一个字符串 string = "python修炼第一期.html"，请写程序从这个字符串里获得.html前面的部分
# 7, "this is a book",请将字符串里的book替换成apple
print('=' * 10, '第一题', '=' * 10)
print('abcd'.upper())
print('abcd'.index('cd'))
for item in 'a,b,c,d'.split():
    print(item)
print('{name}喜欢{fruit}'.format(name='李雷', fruit=''))
string = "Python is good"
print(string.replace('Python', 'python'))
print('this is a book'.replace('book', 'apple'))

# 题目：
# 已知一个列表
# lst = [1,2,9,4,5]
# 1, 求列表的长度
# 2, 判断6 是否在列表中
# 3, lst + [6, 7, 8] 的结果是什么？
# 4, lst*2 的结果是什么
# 5, 列表里元素的最大值是多少
# 6, 列表里元素的最小值是多少
# 7, 列表里所有元素的和是多少
# 8, 在索引1的后面新增一个的元素10
# 9, 在列表的末尾新增一个元素20
print('=' * 10, '第二题', '=' * 10)
lst = [1, 2, 9, 4, 5]
print('列表{}总长{}'.format(lst, len(lst)))
print('6在列表{}中'.format(lst) if 6 in lst else "6不在列表中")
print(lst + [6, 7, 8])
print(lst * 2)
print('最大值', max(lst), '最小值', min(lst))
print('总和', sum(lst))
print(lst, end=' ')
lst.insert(1, 10)
print(lst)
lst.append(20)
print(lst)
# 题目：
# lst = [1, [4, 6], True]
# 请将列表里所有数字修改成原来的两倍
# 只有一个数字
print('=' * 10, '第三题', '=' * 10)
lst = [1, [4, 6], True]

# for i in range(0,len(lst)):
for item in lst:
    if type(item) in (type(int()), type(float())):
        lst[lst.index(item)] = 2 * item
print(lst)

# 题目：
# 字典内容如下
# dic = {
#     'python': 95,
#     'java': 99,
#     'c': 100
# }
# 用程序解答下面的题目
# 字典的长度是多少
# 请修改'java' 这个key对应的value值为98
# 删除 c 这个key
# 增加一个key-value对，key值为 php, value是90
# 获取所有的key值，存储在列表里
# 获取所有的value值，存储在列表里
# 判断 javascript 是否在字典中
# 获得字典里所有value 的和
# 获取字典里最大的value
# 获取字典里最小的value
# 字典 dic1 = {'php': 97}， 将dic1的数据更新到dic中
print('=' * 10, '第四题', '=' * 10)

dic1 = {'php': 97}

dic = {
    'python': 95,
    'java': 99,
    'c': 100
}


def answer():
    dicin = dic
    print('字典{}长{}'.format(dicin, len(dicin)))
    dicin['java'] = 98
    del dicin['c']
    dicin['php'] = 90
    dic_key_lst = list(dicin.keys())
    dic_value_list = list(dicin.values())
    if 'javascript' in set(dic_key_lst) | set(dic_value_list):
        print("javascript在字典中")
    else:
        print("javascript不在字典中")
    print('所有value的和', sum(dicin.values()))
    print('最大的value', max(dicin.values()))
    print('最小的value', min(dicin.values()))
    for x, y in dic1.items():
        dic[x] = dic1[x]
    print(dic)


answer()

# 题目：
# 寻找组合
# lst1 = [3, 6, 1, 8, 1, 9 , 2]
# lst2 = [3, 1, 2, 6, 4, 8, 7]
# 从两个列表里各取1个数，如果这两个数的和等于10，则以元组的方式输出这两个数
print('=' * 10, '第五题', '=' * 10)

lst1 = [3, 6, 1, 8, 1, 9, 2]
lst2 = [3, 1, 2, 6, 4, 8, 7]
for x in lst1:
    for y in lst2:
        if x + y == 10:
            print((x, y))

# 题目：
#
#
#
# 使用input函数接收用户输入的整数，如果是偶数，则使用print函数输出"你输入的是一个偶数",
# 反之输出"你输入的是一个奇数"，用户可以输入多次，直到输入quit时程序退出
print('=' * 10, '第六题', '=' * 10)
while True:
    tem = input('请正确输入：输入整数，则判断奇偶；输入“quit”则退出')
    if tem.isdigit():
        inttem = int(tem)
        print('这个数是偶数' if inttem % 2 == 0 else '这个数不是偶数')
    elif tem == 'quit':
        break
    else:
        print('输入错误！')
# 题目：
# 有五个数字：1、2、3、4、5，能组成多少个互不相同且无重复数字的两位数？各是多少？
# 结果类似于这样：
# ```
# 12
# 13
# 21
# ...
# ```
print('=' * 10, '第七题', '=' * 10)
lst7 = [1, 2, 3, 4, 5]
lst7 = list(set(lst7))
count_index = len(lst7) * (len(lst7) - 1)
lst72 = []
for x in range(0, len(lst7)):
    for y in range(0, len(lst7)):
        if lst7[x] == 0 or lst7[x] == lst7[y]:
            continue
        else:
            lst72.append(lst7[x] * 10 + lst7[y])
print('共有{}个无重复数字的两位数，包括：{}'.format(count_index, lst72))
# 题目：
# 假设每个月固定 30 天，当我输入一个时间格式的时候，得到是一年当中的第多少天。
# 比如：输入 `2020/1/3` , 得到：`3`
print('=' * 10, '第七题', '=' * 10)


def days():
    try:
        date = input('请输入日期：格式xxxx/xx/xx')
        year, month, day = date.split('/')
        sum = (int(month) - 1) * 30 + int(day)
        print('这个日期是{}年中的第{}天'.format(year, sum))
    except (TypeError, ValueError):
        print("输入错误，程序异常退出！！")


days()
# 题目：

# 查找敏感词。 为了净化网络环境，出台了一批新的敏感词 sensitive_words, 请对文本 text 进行筛查，统计
# 每个敏感词出现的频率。
# sensitive_words = ['犯事', '同人', '酒吧']
# text = """生活中，若在同人酒吧犯事出现了，、对一个非常尴尬的事实，那就是， 生活中，
# 若在同人酒吧犯事出现了，我们就不得不考虑它出现了的事实。 对我个人而言，在同人酒吧犯事不仅仅是一个重大的事件，
# 还可能会改变我的人生。 既然如何。
# 　　所谓在同人酒吧犯事，关键是在同人酒吧犯事需要如何写。 """

# 打印：
# ```
# 犯事：3 次
# 同人： 2次
# 酒吧： 4次
print('=' * 10, '第八题', '=' * 10)
text = """生活中，若在同人酒吧犯事出现了，、对一个非常尴尬的事实，那就是， 生活中，
若在同人酒吧犯事出现了，我们就不得不考虑它出现了的事实。 对我个人而言，在同人酒吧犯事不仅仅是一个重大的事件，
还可能会改变我的人生。 既然如何。
所谓在同人酒吧犯事，关键是在同人酒吧犯事需要如何写。 """
sensitive_words = ['犯事', '同人', '酒吧']


def worn_count(textstr, sensitive_word_list):
    sensitive_word_list = list(set(sensitive_word_list))
    sensitive_dict = dict(zip(list(range(0, len(sensitive_word_list))), sensitive_word_list))
    for i in range(0, len(sensitive_word_list)):
        print('{}：{}次'.format(sensitive_dict[i], textstr.count(sensitive_dict[i])))


worn_count(text, sensitive_words)

# 题目：
# 斐波那契数列经常在面试题当中出现。固定指这一串数列：0、1、1、2、3、5、8、13、21、34、……
# 0 之后，后一个数等于前两个数的和。
# 给定一个数字 3以上的数字 n, 请打印出到 n 的斐波那契数列。
# n = 3, 打印:
# ```
# 0
# 1
# 1
# ```
# 第i项为fblq(i)：
#       i=1 0； i=2 1; i>2 fblq(i-1)+fblq(i-2)
print('=' * 10, '第九题', '=' * 10)


def fblqx(num):
    '''计算第num项的数'''
    if num == 1:
        return 0
    if num == 2:
        return 1
    if num > 2:
        return fblqx(num - 1) + fblqx(num - 2)


def fblq(num):
    '''打印到num项的数列'''
    print("打印裴波拉起数列前{}项：\n```".format(int(num)))
    i = 0
    while i < num:
        print(fblqx(i + 1))
        i += 1
    print("```")


fblq(15)
