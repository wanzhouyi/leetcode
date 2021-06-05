# cmp_to_key

## 入门级排序

python的列表提供了sort方法，下面是该方法的一个示例

```python3
lst = [(9, 4), (2, 10), (4, 3), (3, 6)]
lst.sort(key=lambda item: item[0])
print(lst)
```

sort方法的key参数需要设置一个函数，这个函数返回元素参与大小比较的值，这看起来没有问题，但如果想实现更加复杂的自定义排序，就不那么容易了。

## 高阶排序

前面例子的排序规则是根据元组里第一个元素的大小进行排序，我现在修改规则，如果元组里第一个元素是奇数，就用元组里第一个元素进行排序，如果元组里第一个元素是偶数，则用这个元组里的第二个元素进行大小比较，面对这样的需求，列表的sort方法无法满足。

对于这种情形，可以使用 **functools.cmp_to_key** 来解决

```python3
from functools import cmp_to_key
lst = [(9, 4), (2, 10), (4, 3), (3, 6)]

def cmp(x, y):
    a = x[0] if x[0] %2 == 1 else x[1]
    b = y[0] if y[0] %2 == 1 else y[1]

    return 1 if a > b else -1 if a < b else 0

lst.sort(key=cmp_to_key(cmp))
print(lst)
```

仍然使用sort进行排序，我实现了一个cmp函数，该函数实现了需求中所提到的要求，该函数最终要返回两个元组比较的大小关系

## 示例

```python3
from functools import cmp_to_key 
L=[9,2,23,1,2]
 
sorted(L,key=cmp_to_key(lambda x,y:y-x))
输出：
[23, 9, 2, 2, 1]
 
 
sorted(L,key=cmp_to_key(lambda x,y:x-y))
输出：
[1, 2, 2, 9, 23]
```

## cmp_to_key的实现

其实cmp_to_key的实现非常简单

```python3
def cmp_to_key(mycmp):
    """Convert a cmp= function into a key= function"""
    class K(object):
        __slots__ = ['obj']
        def __init__(self, obj):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        __hash__ = None
    return K
```

它在内部定义了一个类K，
并使用我传入的cmp函数完成了比较关系运算符的重载，函数返回的是一个类，而sort函数的key需要的是一个函数，看起来矛盾，但在python中，这样做完全可行，因为类和函数都是callable的，这里把类当成了函数来用。

在本篇第一段代码中

```python3
lst.sort(key=lambda item: item[0])
```

lambda表达式生成的匿名函数返回的是元组的第一个元素进行大小比较，而现在，cmp_to_key返回的是类K，参与比较的是K的对象，由于K已经实现了比较关系运算符重载，且算法就是我刚刚实现的cmp函数，这样就最终实现了自定义排序。

## 实例

### 力扣题目：179.最大数

> 给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。  
> 注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。
>
>示例 1：  
> 输入：nums = [10,2]  
> 输出："210"
>
>示例 2：  
> 输入：nums = [3,30,34,5,9]  
> 输出："9534330"
>
>示例 3：  
> 输入：nums = [1]  
> 输出："1"
>
>示例 4：  
> 输入：nums = [10]  
> 输出："10"
>
>提示：
>
>1 <= nums.length <= 100  
> 0 <= nums[i] <= 109
>
>来源：力扣（LeetCode）
> 链接：https://leetcode-cn.com/problems/largest-number
> 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出>处。

### 题目分析

这道题中列表nums中两个值的相对位置并不能由单一num决定，而是说 x与y拼接比y与x拼接的值大，那么就用[x,y]的顺序，否则用[y,x]的顺序。此时就是所谓的：单个元素并没有一个绝对的大小的情况

### 代码

```python3
from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums):
        ret = map(str, nums)

        def cmp(a, b):
            if a + b >= b + a:
                return 1
            else:
                return -1
        ret = sorted(ret, key=cmp_to_key(cmp), reverse=True)
        return ''.join(ret) if ret[0] != '0' else '0'
```