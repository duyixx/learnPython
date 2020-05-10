"""
    @ 功能：day10作业（异常）
    @ author：古城
    @ create：20200510 22:00
"""
import sys

# 1. 异常捕获的语法是什么样的？    请列举你会的错误类型。
# 1. 格式：
"""
try:
    捕获代码
except ErrorType as alias:
    抛出ErrorType时执行代码
else:
    没有抛出该异常时执行的代码
finally:
    始终执行的代码
    """
print('我会的错误类型{}'.format(
    [ZeroDivisionError, KeyError, ValueError, TypeError, IOError, ImportError, IndexError, AttributeError,
     FileExistsError,
     FileNotFoundError, NameError, Exception]))


# 2. 输入用户的体重身高，计算 bmi, (规则前面作业有） 考虑异常情况

def func_bmi(height, weight):
    '''函数用于计算bmi指数并判断健康情况；height为身高（m），weight为体重（kg）'''
    try:
        bmi = float(weight) / float(height) ** 2
        result = {1: "过轻，娇柔细弱", 2: "正常", 3: "过重", 4: "肥胖", 5: "严重肥胖，你嫁不出去了"}
    except ZeroDivisionError:
        print('体重不能为0')
    except ValueError:
        print('错误！你只能输入数字的身高和体重')
    except UnboundLocalError:
        print('错误！请正确输入身高和体重')
    else:
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

func_bmi(3  ,1)



# 3.编写如下程序优化去生鲜超市买橘子程序
#
# a.收银员输入橘子的价格，单位：元／斤
# b.收银员输入用户购买橘子的重量，单位：斤
# c.计算并且 输出 付款金额
# 新需求：
# d.使用捕获异常的方式，来处理用户输入无效数据的情况
def price_calc():
    """功能：用于根据输入的橘子单价和重量计算橘子的应收款"""
    while 1:
        try:
            price = input('请输入橘子价格（元/斤）：')
            if not (price.count('.')<2 and price.replace(".","").isdigit()): #不是由小于两个小数点+纯数字组成的输入，则抛出异常Exception
                raise Exception
        except Exception:
            print('输入错误，请正确输入单价')
            continue            # 输入错误时要求重新输入
        else:
            while True:
                try:
                    weight = input('请输入橘子重量（斤）')
                    if not (price.count('.')<2 and price.replace(".","").isdigit()):
                        raise Exception
                except Exception:
                    print('请正确输入橘子重量')
                    continue
                else:
                    break
        break
    print('应收：%.2f'%(float(price)*float(weight)))

price_calc()
