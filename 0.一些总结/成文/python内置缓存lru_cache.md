# lru_cache

## LRU算法原理

LRU (Least Recently Used，最近最少使用)
算法是一种缓存淘汰策略。其根据数据的历史访问记录来进行淘汰，核心思想是，“如果数据最近被访问过，那么将来被访问的几率也更高”。该算法最初为操作系统中一种内存管理的页面置换算法，主要用于找出内存中较久时间没有使用的内存块，将其移出内存从而为新数据提供空间。

## python中的LRU

Python 的 3.2 版本中，引入了一个非常优雅的缓存机制，即 functool 模块中的 lru_cache
装饰器，可以直接将函数或类方法的结果缓存住，后续调用则直接返回缓存的结果。lru_cache 原型如下：

> @functools.lru_cache(maxsize=None, typed=False)

使用 functools 模块的 lur_cache 装饰器，可以缓存最多 maxsize 个此函数的调用结果，从而提高程序执行的效率，特别适合于耗时的函数。**参数 maxsize
为最多缓存的次数，如果为 None，则无限制，设置为 2 的幂 时，性能最佳；如果 typed=True（注意，在 functools32 中没有此参数），则不同参数类型的调用将分别缓存，例如 f(
3) 和 f(3.0)**。

## python lru_cache示例

```python3
from functools import lru_cache


@lru_cache(None)
def add(x, y):
    print("calculating: %s + %s" % (x, y))
    return x + y


print(add(1, 2))
print(add(1, 2))
print(add(2, 3))
```

输出结果：
> calculating: 1 + 2  
3  
3  
calculating: 2 + 3  
5

从结果可以看出，当第二次调用 add(1, 2) 时，并没有真正执行函数体，而是直接返回缓存的结果。

## 注意事项

1. 缓存是按照参数作为键
2. 所有参数必须可哈希hash

