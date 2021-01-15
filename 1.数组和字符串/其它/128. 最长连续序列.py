"""
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。



进阶：你可以设计并实现时间复杂度为O(n) 的解决方案吗？



示例 1：

输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
示例 2：

输入：nums = [0,3,7,2,5,8,4,6,0,1]
输出：9


提示：

0 <= nums.length <= 104
-109 <= nums[i] <= 109

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-consecutive-sequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
import heapq


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        heapq.heapify(nums)
        stack = []
        length = 0
        while nums:
            num = heapq.heappop(nums)
            if stack and num == stack[-1]:
                continue
            if stack and num - 1 != stack[-1]:
                length = max(length, len(stack))
                stack.clear()
            stack.append(num)
        length = max(length, len(stack))
        return length


if __name__ == '__main__':
    s = Solution()
    print(s.longestConsecutive(nums=[100, 4, 200, 1, 3, 2]))
    print(s.longestConsecutive(nums=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
    print(s.longestConsecutive(nums=[]))
    print(s.longestConsecutive([1, 2, 0, 1]))
    import random as r

    print(s.longestConsecutive([r.randint(80, 100) for _ in range(10 ** 4)]))
