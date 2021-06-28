"""
给定一个整数数组 nums，按要求返回一个新数组counts。
数组 counts 有该性质： counts[i] 的值是 nums[i] 右侧小于nums[i] 的元素的数量。

示例：

输入：nums = [5,2,6,1]
输出：[2,1,1,0] 
解释：
5 的右侧有 2 个更小的元素 (2 和 1)
2 的右侧仅有 1 个更小的元素 (1)
6 的右侧有 1 个更小的元素 (1)
1 的右侧有 0 个更小的元素

提示：

0 <= nums.length <= 10^5
-10^4<= nums[i] <= 10^4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        from sortedcontainers import SortedList
        n = len(nums)
        sl = SortedList()
        ans = []
        for i in range(n - 1, -1, -1):
            idx = sl.bisect_left(nums[i])
            ans.append(idx)
            sl.add(nums[i])
        return ans[::-1]
