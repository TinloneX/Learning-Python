#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python ---> java 类比学习笔记 之 基础篇
print('中文')
print(len('中文'))  # String.length()

# ---------------------------------------
# 可变有序表（集合）
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
classmates.append('tony')  # 类似List.add(Object)
print(classmates)
classmates.insert(1, 'piano')  # 类似List.add(index,Object)
print(classmates)
classmates.pop()  # 类似List.remove(lastIndex)
print(classmates)
classmates.pop(1)  # 类似List.remove(index)
print(classmates)
# 不可变有序表（元组）
a = (1)  # 计算歧义
print(a)
a = (1,)  # 消除歧义
print(a)
a = (1, '2', ['c', 'd'])  # 元素类型可以不同，类似于List<Object>
print(a)
a[2][0] = 'f'  # 元组定义后不可变，指的是指向（地址）不变，若元素本身可变而发生变化，元组实际并未变化
print(a)

# ---------------------------------------
age = 20
if age > 40:  # 类比于 if(age > 40){}
    print('duang')
elif age >= 18:  # 类比于 else if(age >= 18){}
    print('your age is %d, %s' % (age, 'adult'))  # 等同于System.out.println(String.format("*** %d %s",age,"adult"))
else:
    print('go back home & do your homework !')
if []:  # 类比于 new Object[]{}.isEmpty() 或 Array.length >= 0
    print(False)
if [1]:  # 类比于 {1}.isEmpty()
    print(True)

# ---------------------------------------
by = input('year of birthday:')  # 等待键盘输入，提示语为 *** ***：
year = int(by)  # 类似于 Integer.parseInt(Object) / Integer.valueOf(Object)
age = 2017 - year
if age >= 18:
    print('your age is %d, %s' % (age, 'adult'))

# ---------------------------------------
for name in classmates:  # 类似于 for-each
    print(name)
zum = 0
for x in [1, 2, 3]:
    zum = zum + x
print(zum)
add = 0
for x in range(101):  # range(param) 自动生成自0 - (param - 1) 的等差为1的整数数列
    add = add + x
print(add)
total = 0
for y in range(1, 10001, 2):  # range(start, end - 1, arg1) 自动生成自start - end 的等差为 arg1 的整数数列
    total = total + y
print(total)
# ---------------------------------------
inc = input('0 -> N 累加,N = ')
num = int(inc)
zam = 0
while num > 0:
    zam = zam + num
    num = num - 1
print
'0 -> %s 累加,sum = %d' % (inc, zam)

# --------dict-----字典------类比于 Map---------#dict的key必须是不可变对象#---------
dic1 = {'Michael': 95, 'Bob': 75, 'Tracy': 85}  # 类比于 HashMap 中包含三个键值对
print(dic1)  # 类比于 Map.toString()
print('dic1中Michael的成绩为', dic1['Michael'])  # 类比于 Map.get(key)
dic1['Mark'] = 88  # 类比于 Map.put(key, value)
print('dic1中Mark的成绩为', dic1['Mark'])
dic1['Mark'] = 82  # 类比于 Map.put(key, value) ,会替换该 key 对应的原值，即一键对一值
print('dic1中Mark修改后的成绩为', dic1['Mark'])

if 'piano' in dic1:  # 类比于 Map.contains(key)
    print('piano is in dic1')
else:
    print('piano does not in dic1')

print(dic1.get('Mark'))  # 类比于 Map.get(key)
print(dic1.get('piano'))  # 若有则返回 value，反之返回 None
print(dic1.get('piano', -1))  # 若有则返回 value，反之返回 -1

print('删除 Mark 的数据，移除的数据为', dic1.pop('Mark'))
print('删除 Mark 数据后，字典数据：', dic1)

# 尝试将可变集合作为 dict的key
# dic1[classmates] = 22
# print '将集合作为key',dic1
# 报错信息如下：
# Traceback (most recent call last):
#   File "F:/pythonDemo/test1/pkg1_base/class1_base.py", line 95, in <module>
#     dic1[classmates] = 22
# TypeError: unhashable type: 'list'
# 将不可变tuple元组加入dict
dic1[(1, 2, 3)] = 22
print('将tuple元组(1, 2, 3)作为key', dic1)
# 将含集合的tuple元组加入dict
# dic1[(1, 2, classmates)] = 33
# Traceback (most recent call last):
#   File "F:/pythonDemo/test1/pkg1_base/class1_base.py", line 106, in <module>
#     dic1[(1, 2, classmates)] = 33
# TypeError: unhashable type: 'list'
# print '将tuple元组(1, 2, classmates)作为key',dic1

# -----set----------------------------------
s1 = set(classmates)  # 类比于 HashSet set = new HashSet(Collection);
print(s1)
s1.add('Tony')  # 向 Set 中添加元素
print(s1)
s1.add('Tony')  # 向 Set中添加重复元素，会被去重
print(s1)
s1.remove('Tony')  # 移除Set中的元素
print(s1)

s2 = set([1, 2, 3])
s3 = set([4, 2, 3])
print('执行[1, 2, 3] 且 [4, 2, 3]运算', s2 & s3)
print('执行[1, 2, 3] 或 [4, 2, 3]运算', s2 | s3)

# 尝试将list加入set
# s1.add(classmates)
# print s1
# 报错信息：
# Traceback (most recent call last):
#   File "F:/pythonDemo/test1/pkg1_base/class1_base.py", line 129, in <module>
#     s1.add(classmates)
# TypeError: unhashable type: 'list'

# -----面向对象---------引用与对象-------------------------
a = ['a', 'b', 68]
a.sort()  # 类似于 Collections.sort()
print("[ 'a', 'b', 68]排序后", a)
b = 'abc'
print("b = 'abc' replace新值：", b.replace('a', 'A'))  # 类似于 c = b.replace("a","A") --> c = "Abc",b = "abc"
print("b = 'abc' 执行replace后b值：", b)
