"""
给定一个含有n个正整数的数组和一个正整数s ，找出该数组中满足其和 ≥ s 的长度最小的 连续 子数组，
并返回其长度。如果不存在符合条件的子数组，返回 0。

示例：
输入：s = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组[4,3]是该条件下的长度最小的子数组。

进阶：
如果你已经完成了 O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-size-subarray-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    # 方法一，滑动窗口，40ms
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        import math
        n = len(nums)
        left = 0
        window_sum = 0
        ans = float('inf')
        for right in range(n):
            window_sum += nums[right]
            while window_sum >= s:
                ans = min(ans, right - left + 1)
                window_sum -= nums[left]
                left += 1
        return 0 if math.isinf(ans) else ans


if __name__ == '__main__':
    s = Solution()
    print(s.minSubArrayLen(s=7, nums=[2, 3, 1, 2, 4, 3]))
    # s非常大
    print(s.minSubArrayLen(s=77777, nums=[2, 3, 1, 2, 4, 3]))
    # s非常小
    print(s.minSubArrayLen(s=1, nums=[2, 3, 1, 2, 4, 3]))

