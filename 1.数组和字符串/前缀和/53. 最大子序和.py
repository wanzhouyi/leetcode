"""
给定一个整数数组 nums，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释:连续子数组[4,-1,2,1] 的和最大，为6。
进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    # 方法一，前缀和，40ms，92.55%
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        pre_sum_right = 0
        pre_sum_left = 0
        ans = float('-inf')
        for i in range(n):
            pre_sum_right += nums[i]
            cur_sum = pre_sum_right - pre_sum_left
            ans = max(ans, cur_sum)
            pre_sum_left = min(pre_sum_left, pre_sum_right)
        return ans

    def maxSubArray(self, nums: List[int]) -> int:
        pre = 0
        ans = nums[0]
        for x in nums:
            pre = max(pre + x, x)
            ans = max(ans, pre)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    # print(s.maxSubArray([]))
    print(s.maxSubArray([1]))
