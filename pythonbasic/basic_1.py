#标识符：数字、字母、下划线；不能用数字开头；不能包含关键字
#标识符包含：项目名、模块名、包名、类名、函数名、变量名
    #python是弱类型语言，变量数据类型可直接通过赋值来声明
import keyword

print(keyword.kwlist)
    #变量名：1)要见名知意,2)引用变量前要先声明
age = 10
nianling = 20
class_2019 = 50
#行和缩进：用行控制代码起始；缩进表示层级
if age <18:
    print("younger")
else:
    print('older')
#引号
    #表字符串
s_1="第一行"\
"被拼接的行"
s_2="zfc2"
s_3='''注释1
换行'''
    #三引号能表内容全为字符串：包括空格、换行，可用于注释多行代码
print(s_3)
    #双引号、单引号可用\拼接，可用于注释单行代码
print(s_1)
# 注释快捷键：Ctrl+/
#输出print
print('''111
222
333''','h2',"h3")
#输入
s = input("please input")
print(s)
