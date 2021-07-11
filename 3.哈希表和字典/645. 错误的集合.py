"""
集合 s 包含从 1 到n的整数。不幸的是，因为数据错误，导致集合里面某一个数字复制了成了集合里面的另外一个数字的值，导致集合 丢失了一个数字 并且 有一个数字重复 。

给定一个数组 nums 代表了集合 S 发生错误后的结果。

请你找出重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。

示例 1：

输入：nums = [1,2,2,4]
输出：[2,3]
示例 2：

输入：nums = [1,1]
输出：[1,2]

提示：

2 <= nums.length <= 104
1 <= nums[i] <= 104

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/set-mismatch
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        a = list(range(1, len(nums) + 1))
        a1 = set(a)
        b1 = set(nums)
        lost = a1.difference(b1)
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return [nums[i], lost.pop()]


# =--------------以下是官解----------
class Solution:
    """
    方法一：排序
    将数组排序之后，比较每对相邻的元素，即可找到错误的集合。
    寻找重复的数字较为简单，如果相邻的两个元素相等，则该元素为重复的数字。
    寻找丢失的数字相对复杂，可能有以下两种情况：
        如果丢失的数字大于 1 且小于 n，则一定存在相邻的两个元素的差等于 2，这两个元素之间的值即为丢失的数字；
        如果丢失的数字是 1 或 n，则需要另外判断。
    为了寻找丢失的数字，需要在遍历已排序数组的同时记录上一个元素，然后计算当前元素与上一个元素的差。
    考虑到丢失的数字可能是 1，因此需要将上一个元素初始化为 0。

    当丢失的数字小于 n 时，通过计算当前元素与上一个元素的差，即可得到丢失的数字；

    如果 nums[n−1]!=n，则丢失的数字是 n。

    作者：LeetCode-Solution
    链接：https://leetcode-cn.com/problems/set-mismatch/solution/cuo-wu-de-ji-he-by-leetcode-solution-1ea4/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def findErrorNums(self, nums: List[int]) -> List[int]:
        error_nums = [None, None]
        n = len(nums)
        nums.sort()
        pre = 0
        for i in range(1, n):
            if nums[i] == pre:
                error_nums[0] = pre
            elif nums[i] - pre > 1:
                error_nums[1] = pre + 1
            pre = nums[i]
        if nums[-1] != n:
            error_nums[1] = n
        return error_nums


"""
分析
这道题做不出来的，肯定是上学的时候数学老师长得不够漂亮！

纯数学的角度解题：
sum(nums) - sum(set(nums)) = 重复的数字
(1 + len(nums)) * len(nums) // 2 - sum(set(nums)) = 丢失的数字

循环数组
如何一次for循环获取到重复的数字和丢失的数字呢？

我们需要对数组进行排序
重复的数字就是nums[i + 1] == nums[i]
丢失的数字呢需要分情况考虑
当nums[0] ！= 1，丢失的数字是1
当nums[-1] != len(nums),丢失的数字是len(nums)
排除上面两种场景，那么当nums[i + 1] - nums[i] = 2时，
丢失的数字为nums[i] + 1
哈希表操作

使用Counter将nums转化为一个字典dict
然后for循环1 -- n
没有在dict中找到的数字为丢失的
找到的数字value为2的便是重复的
数学解题

class Solution:
    def findErrorNums(self, nums):
        ln, total = len(nums), sum(set(nums))
        return [sum(nums) - total, (1 + ln) * ln // 2 - total]
循环数组解题

class Solution:
    def findErrorNums(self, nums):
        ln = len(nums)
        repeat = lose = -1
        nums.sort()
        if nums[0] != 1:
            lose = 1
        elif nums[-1] != ln:
            lose = ln
        for i in range(1, ln):
            if nums[i] == nums[i - 1]:
                repeat = nums[i]
            if nums[i] - nums[i - 1] == 2:
                lose = nums[i] - 1
        return [repeat, lose]
哈希表解题

from collections import Counter

class Solution:
    def findErrorNums(self, nums):
        ln = len(nums)
        dic = Counter(nums)
        repeat = lose = -1
        for i in range(1, ln + 1):
            tmp = dic.get(i, 0)
            if tmp == 0:
                lose = i
            elif tmp == 2:
                repeat = i
        return [repeat, lose]

作者：qingfengpython
链接：https://leetcode-cn.com/problems/set-mismatch/solution/645cuo-wu-de-ji-he-shu-zu-bian-li-ha-xi-94hcp/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。"""

if __name__ == '__main__':
    s = Solution()
    print(s.findErrorNums(nums=[1, 2, 2, 4]))
    print(s.findErrorNums(nums=[1, 1]))
    print(s.findErrorNums(nums=[1, 2, 3, 5, 5]))
    print(s.findErrorNums(nums=[1, 2, 3, 5, 6, 6]))
    print(s.findErrorNums(nums=[2, 2, 3, 4]))
