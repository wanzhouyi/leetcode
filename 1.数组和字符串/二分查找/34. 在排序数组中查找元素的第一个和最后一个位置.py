"""
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
    # 方法一，使用bisect，44ms，44.75%
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        import bisect
        left, right = bisect.bisect_left(nums, target), bisect.bisect_right(nums, target)
        # 如果left==target，代表元素存在
        if nums and left < len(nums) and nums[left] == target:
            return [left, right - 1]
        else:
            return [-1, -1]

    # 方法一，手工二分，28ms，99.02%
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def get_left(nums, target):
            left, right = 0, len(nums)
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    right = mid
                elif nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
            return right if nums and right <= len(nums) - 1 and nums[right] == target else -1

        def get_right(nums, target):
            left, right = 0, len(nums)
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] <= target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid
            return right - 1

        left = get_left(nums, target)
        if left != -1:
            return [left, get_right(nums, target)]
        else:
            return [-1, -1]


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        def left_func(nums, target):
            n = len(nums) - 1
            left = 0
            right = n
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] >= target:
                    right = mid - 1
                if nums[mid] < target:
                    left = mid + 1
            return left

        a = left_func(nums, target)
        b = left_func(nums, target + 1)
        if a == len(nums) or nums[a] != target:
            return [-1, -1]
        else:
            return [a, b - 1]


if __name__ == '__main__':
    s = Solution()
    print(s.searchRange(nums=[5, 7, 7, 8, 8, 10], target=8))
    print(s.searchRange(nums=[5, 7, 7, 8, 8, 10], target=6))
    print(s.searchRange(nums=[], target=0))
    # # 单元素用例
    print(s.searchRange(nums=[1], target=1))
    print(s.searchRange(nums=[1], target=2))
    # 多元素用例
    print(s.searchRange([2, 2, 2], 1))
    print(s.searchRange([2, 2, 2], 2))
    print(s.searchRange([2, 2, 2], 3))
