"""
35. 搜索插入位置
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
你可以假设数组中无重复元素。

示例 1:
输入: [1,3,5,6], 5
输出: 2

示例 2:
输入: [1,3,5,6], 2
输出: 1

示例 3:
输入: [1,3,5,6], 7
输出: 4

示例 4:
输入: [1,3,5,6], 0
输出: 0
"""
from typing import List


class Solution:
    # 方法一，使用系统函数，32 ms
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        排序数组,可使用此方法最快解答
        """
        import bisect
        return bisect.bisect_left(nums, target)

    # 方法二，使用暴力法，44ms
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        不要看不起暴力解
        """
        for idx, num in enumerate(nums):
            if num >= target:
                return idx
        return len(nums)

    # 方法三，手工二分，44ms
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        1.left<=right版本,左闭右闭区间，退出循环时left=right+1
        2.注意题目中已标明，可以假设无重复元素
        3.由于边界条件易错，用elif列举出所有情况
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        # return right+1
        return left

    # 方法四，手工二分，36ms
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        left<right版本，左闭右开区间，退出循环时left=right
        """
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
        return left


if __name__ == '__main__':
    s = Solution()
    # 能找到元素的用例
    print(s.searchInsert([1, 3, 5, 6], 5))
    # 找不到元素的用例
    print(s.searchInsert([1, 3, 5, 6], 2))
    # 在数组右边的用例
    print(s.searchInsert([1, 3, 5, 6], 7))
    # 在数组左边的用例
    print(s.searchInsert([1, 3, 5, 6], 0))
