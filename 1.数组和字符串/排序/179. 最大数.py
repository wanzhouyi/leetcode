"""
给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。

注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。



示例 1：

输入：nums = [10,2]
输出："210"
示例2：

输入：nums = [3,30,34,5,9]
输出："9534330"
示例 3：

输入：nums = [1]
输出："1"
示例 4：

输入：nums = [10]
输出："10"


提示：

1 <= nums.length <= 100
0 <= nums[i] <= 109

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/largest-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from functools import cmp_to_key
from typing import List


class Solution:

    def largestNumber(self, nums: List[int]) -> str:
        ret = map(str, nums)

        def cmp(a, b):
            if a + b >= b + a:
                return 1
            else:
                return -1

        ret = sorted(ret, key=cmp_to_key(cmp), reverse=True)
        return ''.join(ret) if ret[0] != '0' else '0'


# 以下是官解

'''
方法一：排序
思路与算法

要想组成最大的整数，一种直观的想法是把数值大的数放在高位。
于是我们可以比较输入数组的每个元素的最高位，最高位相同的时候比较次高位，以此类推，完成排序，然后把它们拼接起来。
这种排序方式对于输入数组 没有相同数字开头 的时候是有效的，例如 [45, 56, 81, 76, 123]。

下面考虑输入数组 有相同数字开头 的情况，例如 [4,42] 和 [4,45]。

对于 [4,42]，比较 442 > 424，需要把 4 放在前面；
对于 [4,45]，比较 445 < 454，需要把 45 放在前面。
因此我们需要比较两个数不同的拼接顺序的结果，进而决定它们在结果中的排列顺序。

由于需要拼接以后才能决定两个数在结果中的先后顺序，N 个数就有 N! 种拼接的可能，
我们是不是需要先得到 N 个数的全排列以后，再选出最大的呢？答案是没有必要。
上述排序规则满足传递性，两个元素比较就可以确定它们在排序以后的相对位置关系。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/largest-number/solution/zui-da-shu-by-leetcode-solution-sid5/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
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
