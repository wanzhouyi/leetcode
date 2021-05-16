### 一、异或运算的定义

如果a、b两个值不相同，则异或结果为1。如果a、b两个值相同，异或结果为0。  
在python中用^表示，如下代码（注意是二进制表示）。

~~~python3
1 ^ 0  # 结果为1，因为1和0不同
0 ^ 1  # 结果为1，因为0和1不同
1 ^ 1  # 结果为0，因为1和1相同
0 ^ 0  # 结果为0，因为0和0相同
~~~

### 二、异或运算的性质

* 交换律：A ^ B = B ^ A;
* 结合律：A ^ (B ^ C) = (A ^ B) ^ C;
* 恒等律：X ^ 0 = X;
* 归零律：X ^ X = 0;
* 自反：A ^ B ^ B = A ^ 0 = A;
* 对于任意的 X： X ^ (-1) = ~X；
* 如果 A ^ B = C 成立，那么 A ^ B = C，B ^ C = A；

### 三、异或运算的实例

以  *5 ^ 3* 为例，理解python中异或运算的过程 首先python会将5和3转换为二进制：101^011 然后按位求异或结果：110 最后转换成十进制，结果为6

### 三、异或运算的应用

1. 交换两个数

~~~python3
a, b = 5, 3
a = a ^ b
b = a ^ b
a = a ^ b
print(a, b)
~~~

不出所料，最后的输出是a=3和b=5。  
这个用法实际上利用了异或的这个特性：

~~~
x^0=x
x^x=0
~~~

2. 消除影响([1720. 解码异或后的数组](https://leetcode-cn.com/problems/decode-xored-array))
   简单来说，就是对一个数异或两次，就能消除这个数引发的影响了。

~~~python3
def decode(self, encoded: list[int], first: int) -> list[int]:
    ans = [first]
    for num in encoded:
        ans.append(ans[-1] ^ num)
    return ans
~~~

类似的题目还有 [136. 只出现一次的数字](https://leetcode-cn.com/problems/single-number)
3.计算汉明距离( [461\. 汉明距离](https://leetcode-cn.com/problems/hamming-distance/))

~~~python3
def hammingDistance(self, x, y):
    return bin(x ^ y).count('1')
~~~
