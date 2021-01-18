"""
给定一个n个元素有序的（升序）整型数组nums 和一个目标值target ，
写一个函数搜索nums中的 target，如果目标值存在返回下标，否则返回 -1。

示例 1:

输入: nums = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 出现在 nums 中并且下标为 4

示例2:

输入: nums = [-1,0,3,5,9,12], target = 2
输出: -1
解释: 2 不存在 nums 中因此返回 -1

提示：

你可以假设 nums中的所有元素是不重复的。
n将在[1, 10000]之间。
nums的每个元素都将在[-9999, 9999]之间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-search
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    # 方法一，使用index，268 ms，78.1%
    def search(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except ValueError:
            return -1

    # 方法二，使用bisect，328 ms，13.77%
    def search(self, nums: List[int], target: int) -> int:
        import bisect
        insert_index = bisect.bisect_left(nums, target)

        return -1 if (not nums) \
                     or (insert_index > len(nums) - 1) \
                     or (nums[insert_index] != target) else insert_index

    # 方法三，手撕二分，448 ms，5.32%
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left += 1
        return -1

    # 方法三，手撕二分（续)，344  ms，7.56%
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left += 1
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.search(nums=[-1, 0, 3, 5, 9, 12], target=9))
    print(s.search(nums=[-1, 0, 3, 5, 9, 12], target=2))
    print(s.search(nums=[-1, 0, 3, 5, 9, 12], target=-8))
    print(s.search(nums=[], target=1))
    print(s.search(nums=[1], target=1))
    print(s.search(nums=[1], target=-1))
    print(s.search(nums=[1], target=3))
    print(s.search(nums=[1, 2], target=1))
