# coding = utf-8
# auth: SSRGray
# tuple: 有序数组，可重复，用()
# 数据类型？储存数据用的
#特性
# # 1：空元组,长度0
# t1 = ()
# print(type(t1))
# print(len(t1))
# # 2：一元素元组要在后面加上逗号，不然会按元素识别
# t2 = (1,)
# print(type(t2))
# print(len(t2))
# # 3：元组元素可以是任意数据类型
# t3 = (1,0.0002,'str',True,(1,),[2,],{'key1':'15'},{'set1','set2'})
# print(type(t3))
# print(len(t3))
# # 4 元组的操作：特性：有序不可变（有序：有索引号；不可变：元素值不能更改和删除）
t4 = (1,0,0.0002,'str',True,True,False,(1,),[2,],{'key1':'15'},{'set1','set2'})
# print(t4[-2].get('key1')[1])      #嵌套取值
# print(t4[2:7:2])                   #切片tuple[start:end:step]
# 常用方法：
##获取元素的索引值.index(元素)
# print(t4.index(0.0002))     #结果：2
# print(t4.count(1))          #结果是：3：把1当做True来计数了
# print(t4.count(0))          #结果是：2：把0当做Flase来计数了
