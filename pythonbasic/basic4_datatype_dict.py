# -*- conding: utf-8 -*-
# @Author   : SSRGray
''' 字典：无序，元素为键值对key:value，key唯一且不可变且不能用list、dict,value无限制'''

'''特点：'''
'''1：空字典'''
# d = {}
# print(type(d))
'''2：key不能用list和dict类型'''
d1 = {1:10,0.02:0.022,'name':['a','b','c'],('tuple1',):{1:1},}
     # []:2}  #TypeError: unhashable type: 'list'
# print(d1)
'''3：元素存储是无序：指输出顺序不同于插入值的顺序,要想有序可用Ordereddict'''
# for i,k in d1.items():
#     print(i,k)
'''4：访问元素，根据key和value'''
# print(d1[1])
'''5:key唯一（1→True，0→Flase,遇到重复的key，会用前面的key和后面的value）'''
d2 = {1:10,0:0.022,True:['a','b','c'],False:{1:1},}
# print(d2)
# print(len(d2))
'''6:遍历字典.items()、.keys()、.values()'''
##.fromkeys()
d3 = dict.fromkeys(['key1','key2','key3'])##以列表元素为key创建值为空的字典
#字典元素操作：
d4 = {1:'python29','teacher':['苍老师','浅田结梨','天海冀'],'vip':{'A':'路人甲','B':'路人乙','C':'张三'},'score':(88,99,100)}
##查：根据key进行查询、d.get(key[,default])：default，间不存在时返回这个元素，缺省为None
print(d1,'\n',d2,'\n',d3,'\n',d4)
'''
改：dict[oldkey] = newvalue
增：dict[newkey] = newvalue
删：dict.pop(key)删除键值对，  dict.clear()清空字典，  dict.popitem()随机删除某个键值对'''
'''其它用法：'''
#items()   以列表返回可遍历的键值对元组数组
# print(d4.items())
# print(type(d4.items()))
#keys()    以列表返回字典所有的键
# print(d4.keys())
# print(type(d4.keys()))
#values()  以列表返回字典所有的值
#pop(key)  按key删除指定键值对
# d4.pop(1)
#del dict[key]   按key删除指定键值对
# del d4['teacher']
print(d4)
