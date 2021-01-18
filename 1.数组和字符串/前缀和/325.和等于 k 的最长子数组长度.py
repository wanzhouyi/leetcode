"""
给定一个数组 nums 和一个目标值 k，找到和等于 k 的最长子数组长度。如果不存在任意一个符合要求的子数组，则返回 0。
注意:
nums 数组的总和是一定在 32 位有符号整数范围之内的。

示例:
示例 1:

输入: nums = [1, -1, 5, -2, 3], k = 3
输出: 4
解释: 子数组 [1, -1, 5, -2] 和等于 3，且长度最长。
示例 2:

输入: nums = [-2, -1, 2, 1], k = 1
输出: 2
解释: 子数组 [-1, 2] 和等于 1，且长度最长。
进阶:

你能使时间复杂度在 O(n) 内完成此题吗?
"""
from typing import List


class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        ans = 0
        pre_sum = [0]
        for index in range(len(nums)):
            pre_sum.append(pre_sum[-1] + nums[index])
        for index in range(1, len(pre_sum)):
            try:
                if k == 0:
                    left = 1 + pre_sum[1:].index(pre_sum[index] - k)
                else:
                    left = pre_sum.index(pre_sum[index] - k)
                ans = max(ans, index - left)
            except ValueError:
                pass
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.maxSubArrayLen(nums=[1, -1, 5, -2, 3], k=3))
    print(s.maxSubArrayLen(nums=[1, -1, 5, -2, 3], k=0))
    print(s.maxSubArrayLen(nums=[-2, -1, 2, 1], k=1))
