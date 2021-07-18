### python中进行字符串排序

python中没有直接的方法对字符串进行排序，原因是字符串类型是不允许直接修改元素的。  
因此字符串排序的主要方法是将字符串转换成字符数组， 然后借用sorted函数进行排序， 最后用join方法重新拼装字符串。

```python
chars = 'python'
# 写法一
ls = list(chars)
ls.sort()
print(''.join(ls))

# 写法二
print(''.join(sorted(chars)))
```

输出结果
> hnopty

### 进阶，如何根据字符串数组长度排序

我们可以使用sort方法和sorted函数根据长度进行排序，方法是将键作为参数传递给排序的方法。

```python
# 字符串列表
strings = ['Python', 'C', 'Java', 'Javascript', 'React', 'Django', 'Spring']
# 以升序对列表进行排序-长度
strings.sort(key=len)
# 打印排序列表
print(strings)
```

输出结果
> ['C', 'Java', 'React', 'Python', 'Django', 'Spring', 'Javascript']

我们可以将任何函数传递给key参数。sort方法将根据给定给键参数的函数的返回值对列表进行排序。同样的道理也适用于排序后的函数。

### 进阶，如何根据字符串的值排序

```python
# 字符串列表
strings = ['7', '34', '3', '23', '454', '12', '9']
# 以升序对列表进行排序-int值
sorted_strings = sorted(strings, key=int)
# 打印排序列表
print(sorted_strings)
```

输出结果
> ['3', '7', '9', '12', '23', '34', '454']

### 进阶，如何忽略大小写排序

#### 暴力写法

```python
strs = ['the', 'stirng', 'Has', 'many', 'line', 'In', 'THE', 'fIle']
# 将字符串列表，生成元组，（忽略大小写的字符串，字符串）
listtemp = [(x.lower(), x) for x in strs]
# 对元组排序，因为元组为：（忽略大小写的字符串，字符串），就是按忽略大小写的字符串排序
listtemp.sort()
# 排序完成后，返回原字符串的列表  
print([x[1] for x in listtemp])
```

输出结果
> ['fIle', 'Has', 'In', 'line', 'many', 'stirng', 'THE', 'the']

#### 使用内置函数

```python
strs = ['the', 'stirng', 'Has', 'many', 'line', 'In', 'THE', 'fIle']
print(sorted(strs, key=str.lower))
```

输出结果
> ['fIle', 'Has', 'In', 'line', 'many', 'stirng', 'THE', 'the']  
