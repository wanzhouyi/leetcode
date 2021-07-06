## python的集合操作

* set是一个无序不重复的序列
* 可以用 { } 或者 set( ) 函数创建集合
* 集合存放不可变类型（字符串、数字、元组）  
  注意：创建一个空集合必须用 set( ) 而不是 { } ，因为 { } 是用来创建一个空字典

1. 添加单个元素

```python3
# 使用 add()方法，往set里面添加元素
num_set = {1, 2, 3, 4}
# 添加一个不存在的元素
num_set.add(5)
print(num_set)
# 添加一个存在的元素
num_set.add(3)
print(num_set)

# 结果：
# {1, 2, 3, 4, 5}  
# {1, 2, 3, 4, 5}

```

2. 添加多个元素

```python
# 批量往set里面添加元素
# 使用update()方法可以一次性给set添加多个元素
num_set = {1, 2, 3}
num_set.update({3, 4, 5})
print(num_set)

# 结果：
# {1, 2, 3, 4, 5}  
```

3. 删除集合元素

```python
# set提供了remove()方法来删除set中的元素
num_set = {1, 2, 3}
num_set.remove(2)
print(num_set)

# 结果
# {1, 3}  
```

注意  
如果删除不存在的元素，会报错

```python
num_set = {1, 2, 3}
num_set.remove(5)
print(num_set)

# 结果
# Traceback (most recent call last):
#   File "E:\test_proj\leetcode\playground.py", line 2, in <module>
#     num_set.remove(5)
# KeyError: 5
```

4. 删除集合元素的推荐方法

```python
# 不会报错的删除方法discard
num_set = {1, 2, 3}
num_set.discard(2)
print(num_set)
num_set.discard(5)
print(num_set)

# 结果：
# {1, 3}  
# {1, 3}
```

5. 随机删除元素

```python
# 随机删除集合中元素
s = {'1', '2', '3'}
s.pop()
print(s)

# 结果
# {'3', '1'}
```

6. 清除所有元素

```python
num_set = {1, 2, 3}
num_set.clear()
print(num_set)
```

7. 判断子集和超集

```python
# 集合的子集和超集
s1 = {1, 2, 3, 4, 5}
s2 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# 判断s1是否为s2的子集
print('s1是否为s2的子集:', s1.issubset(s2))
# 判断s2是否是s1的子集
print('s2是否是s1的子集:', s2.issubset(s1))
# 判断s1是否为s2的超集
print('s1是否为s2的超集:', s1.issuperset(s2))
# 判断s2是否为s1的超集
print('s2是否是s1的超集:', s2.issuperset(s1))

# 结果
# s1是否为s2的子集: True
# s2是否是s1的子集: False
# s1是否为s2的超集: False
# s2是否是s1的超集: True
```

8. 判断是否有重合

```python
# 判断集合是否重合
# set提供isdisjoint() 方法，可以快速判断两个集合是否有重合，
# 如果有重合，返回False，否则返回True
s1 = {1, 2, 3, 4, 5}
s2 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(s1.isdisjoint(s2))

# 结果
# False
```

9. 差集(-)(difference)

```python
# difference求差集 或者用 -
s = {1, 2, 3}
s1 = {3, 4, 5}
# 两种求差集的方法
print('在s中不在s1中:', s.difference(s1))
print('在s1中不在s中:', s1 - s)

# 结果
# 在s中不在s1中: {1, 2}
# 在s1中不在s中: {4, 5}
```

10. 交集(&)(intersection)

```python
s1 = {1, 2, 3}
s2 = {3, 4, 5}
# 同时在集合s1 和 s1 中的元素
print(s1.intersection(s2))
print(s1 & s2)

# 结果
# {3}
# {3}
```

11. 并集(|)(union)

```python
s1 = {1, 2, 3}
s2 = {3, 4, 5}
# 元素在集合 s 中或在集合 s1 中
print(s1.union(s2))
print(s1 | s2)

# 结果
# {1, 2, 3, 4, 5}
# {1, 2, 3, 4, 5}
```

12. 对称差集(^)(sysmmetric_difference)

```python
s1 = {1, 2, 3}
s2 = {3, 4, 5}
# 除集合s1和集合s2共有的以外的元素
print(s1.symmetric_difference(s2))
print(s1 ^ s2)

# 结果
# {1, 2, 4, 5}
# {1, 2, 4, 5}
```

13. 对称差集合更新(symmetric_difference_update)

```python
# 将s2更新到s1中的同时去除s2和s1中相同的元素
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s1.symmetric_difference_update(s2)
print(s1)

# 结果
# {1, 2, 4, 5}
```

14. 交集更新操作(intersection_update )

```python
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s1.intersection_update(s2)
s2.intersection_update(s1)
print(s1)
print(s2)

# 结果
# {3}
# {3}
```