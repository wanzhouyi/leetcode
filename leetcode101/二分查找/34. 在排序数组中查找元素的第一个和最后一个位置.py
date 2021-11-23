"""
34. 在排序数组中查找元素的第一个和最后一个位置
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
如果数组中不存在目标值 target，返回[-1, -1]。
进阶：
你可以设计并实现时间复杂度为O(log n)的算法解决此问题吗？
示例 1：

输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]
示例2：

输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]
示例 3：
输入：nums = [], target = 0
输出：[-1,-1]
提示：

0 <= nums.length <= 105
-109<= nums[i]<= 109
nums是一个非递减数组
-109<= target<= 109

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        import bisect
        left = bisect.bisect_left(nums, target)
        if left == len(nums) or nums[left] != target:
            return [-1, -1]
        right = bisect.bisect_right(nums, target) - 1
        if nums[right] != target:
            return [-1, -1]
        return [left, right]


if __name__ == '__main__':
    s = Solution()
    # print(s.searchRange(nums=[5, 7, 7, 8, 8, 10], target=8))
    # print(s.searchRange(nums=[5, 7, 7, 8, 8, 10], target=4))
    # print(s.searchRange(nums=[5, 7, 7, 8, 8, 10], target=5))
    # print(s.searchRange(nums=[5,5, 7, 7, 8, 8, 10], target=5))
    # print(s.searchRange(nums=[5, 7, 7, 8, 8, 10], target=6))
    # print(s.searchRange(nums=[5, 7, 7, 8, 8, 10], target=10))
    # print(s.searchRange(nums=[5, 7, 7, 8, 8, 10], target=18))
    # print(s.searchRange(nums=[5,5, 7, 7, 8, 8, 10], target=5))
