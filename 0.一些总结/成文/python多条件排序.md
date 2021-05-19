### 引言

假如有一个元组， ls=[(1,2),(2,2),(5,4),(5,3),(8,4)]

1. 如果对此元组进行排序，要求是按第一个元素升序，如果第一个元素相同，按第二个元素的**升序**排列

```python3
ls = [(1, 2), (2, 2), (5, 4), (5, 3), (8, 4)]
ls.sort(key=lambda x: (x[0], x[1]))
print(ls)  # [(1, 2), (2, 2), (5, 3), (5, 4), (8, 4)]
```

2. 如果对此元组进行排序，要求是按第一个元素升序，如果第一个元素相同，按第二个元素的**降序**排列

```python3
ls = [(1, 2), (2, 2), (5, 4), (5, 3), (8, 4)]
ls.sort(key=lambda x: (x[0], -x[1]))
print(ls)  # [(1, 2), (2, 2), (5, 4), (5, 3), (8, 4)]
```

如果有多个条件怎么写呢？ 只需要在写上多个条件就可以了，形如lambda x:(x[0],x[1],……,x[n])

### 原理解析

python的排序算法是归并排序，而归并排序是稳定排序（直白点说，如果两个元素比较不出大小，那么这两个元素的位置是保持不变的）。

### 力扣题目

692.前K个高频单词
* * *

### 一、列表的sort排序函数

函数原型：

         list.sort(key=None,reverse=False)

函数功能：

对原列表进行排序，完成排序后，原列表变为有序列表。默认情况（不传入任何参数时）按字典顺序排序。

函数参数：

(1)key: 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中。指定可迭代对象中的一个元素来进行排序指定排序时使用的单个元素或多个元素、lambda表达式；

(2)reverse：指字排序规则是升序还是降序，默认为升序排序；

### 二、排序示例

1.字符串排序

```python3
def list_sort_string():
    list = ["delphi", "Delphi", "python", "Python", "c++", "C++", "c", "C", "golang", "Golang"]
    list.sort()  # 按字典顺序升序排列
    print("升序:", list)

    list.sort(reverse=True)  # 按降序排列
    print("降序:", list)
```

排序结果：

> 升序: ['C', 'C++', 'Delphi', 'Golang', 'Python', 'c', 'c++', 'delphi', 'golang', 'python']  
降序: ['python', 'golang', 'delphi', 'c++', 'c', 'Python', 'Golang', 'Delphi', 'C++', 'C']

2.数值型排序

```python3
def list_sort_number():
    list = [30, 40, 10, 50, 50.1, 80, 60, 100, 90]
    list.sort()
    print("升序:", list)

    list.sort(reverse=True)
    print("降序:", list)
   ```

排序结果：

> 升序: [10, 30, 40, 50, 50.1, 60, 80, 90, 100]  
降序: [100, 90, 80, 60, 50.1, 50, 40, 30, 10]

3.根据列表中类对象的属性排序

```python3
class element(object):
    def __init__(self, id="", name=""):
        self.id = id
        self.name = name

    def __lt__(self, other):  # override <操作符
        if self.id < other.id:
            return True
        return False

    def __str__(self):  # override __str__
        return "id={0},name={1}".format(self.id, self.name)


def sort_by_attribute():
    list = [element(id="130", name="json"),
            element(id="01", name="jack"), element(id="120", name="tom")]
    list.sort()
    for item in list:
        print(item)
```

由于list.sort()函数在排序时，使用的是小于号对比，所以自定义的数据类型需要override __lt__(小于)函数才能实现排序。

根据element的id属性排序

排序列的结果：

> id=01,name=jack  
id=120,name=tom  
id=130,name=json

4.根据列表中元素的长度排序

```python3
def list_sort_by_length():
    list = ["delphi", "Delphi", "python", "Python", "c++", "C++", "c", "C", "golang", "Golang"]
    list.sort(key=lambda ele: len(ele))  # 按元素长度顺序升序排列
    print("升序:", list)

    list.sort(key=lambda ele: len(ele), reverse=True)  # 按降序排列
    print("降序:", list)
```

借助于lambda表达式，计算list列表中的元素的长度，根据元素的长度进行排序

排序的结果：

> 升序: ['c', 'C', 'c++', 'C++', 'delphi', 'Delphi', 'python', 'Python', 'golang', 'Golang']  
降序: ['delphi', 'Delphi', 'python', 'Python', 'golang', 'Golang', 'c++', 'C++', 'c', 'C']

5.根据列表中元素的多个属性进行排序：

```python3
def two_d_list_sort():
    list = [["1", "c++", "demo"],
            ["1", "c", "test"],
            ["2", "java", ""],
            ["8", "golang", "google"],
            ["4", "python", "gil"],
            ["5", "swift", "apple"]
            ]
    list.sort(key=lambda ele: ele[0])  # 根据第1个元素排序
    print(list)
    list.sort(key=lambda ele: ele[1])  # 先根据第2个元素排序
    print(list)
    list.sort(key=lambda ele: (ele[1], ele[0]))  # 先根据第2个元素排序，再根据第1个元素排序
    print(list)
```

同样借助于lambda表达式完成，当然也可以定义一个与labmda具有相同意义的函数实现排序。

排序结果：

> [['1', 'c++', 'demo'], ['1', 'c', 'test'], ['2', 'java', ''], ['4', 'python', 'gil'], ['5', 'swift', 'apple'], ['8', 'golang', 'google']]  
[['1', 'c', 'test'], ['1', 'c++', 'demo'], ['8', 'golang', 'google'], ['2', 'java', ''], ['4', 'python', 'gil'], ['5', 'swift', 'apple']]  
[['1', 'c++', 'demo'], ['1', 'c', 'test'], ['8', 'golang', 'google'], ['2', 'java', ''], ['4', 'python', 'gil'], ['5', 'swift', 'apple']]

6.动态的根据用户指定的索引进行排序

有时候，在写代码之前，并不知道根据二维表的哪几列排序，而是在程序运行的时候根据输入或配置决定的，为了解决这个动态根据多个列或属性排序的问题，借助了eval()
函数，eval函数能够把字符串编译成python代码并运行，从而达到动态根据多个列或属性排序的目的。

排序结果：

> 排序索引: 0 [['1', 'c++', 'demo'], ['1', 'c', 'test'], ['2', 'java', ''], ['4', 'python', 'gil'], ['5', 'swift', 'apple'], ['8', 'golang', 'google']]  
排序索引: 1 [['1', 'c', 'test'], ['1', 'c++', 'demo'], ['8', 'golang', 'google'], ['2', 'java', ''], ['4', 'python', 'gil'], ['5', 'swift', 'apple']]  
排序索引: 2 [['2', 'java', ''], ['5', 'swift', 'apple'], ['1', 'c++', 'demo'], ['4', 'python', 'gil'], ['8', 'golang', 'google'], ['1', 'c', 'test']]  
排序索引: 1,0 [['1', 'c++', 'demo'], ['1', 'c', 'test'], ['8', 'golang', 'google'], ['2', 'java', ''], ['4', 'python', 'gil'], ['5', 'swift', 'apple']]

综上，基本总结了list.sort的使用的大部分场景，如下：

1、默认排序

2、根据类对象的单个属性进行排序，当然也可以扩展为根据类对象的多个属性进行排序

3、根据元素的固有属性进行排序，如：长度、第N个元素等。为了简单，所以借助了lambda表达式，当然也可以使用普通函数代替lambda表达式

4、动态的根据多个列进行排序，同时借助lambda和eval()函数实现

5、另外相比Python2，Python3取消了sort函数中的 cmp方式，只能用key方式。 所以python2用cmp方式写的函数迁移到python3中需要转换。

> from functools import cmp_to_key  
sort(iterable, key=cmp_to_key(cmp_fun)）
