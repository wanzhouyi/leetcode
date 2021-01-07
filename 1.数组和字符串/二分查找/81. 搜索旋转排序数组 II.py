"""
假设按照升序排序的数组在预先未知的某个点上进行了旋转。
( 例如，数组[0,0,1,2,2,5,6]可能变为[2,5,6,0,0,1,2])。
编写一个函数来判断给定的目标值是否存在于数组中。若存在返回true，否则返回false。

示例1:
输入: nums = [2,5,6,0,0,1,2], target = 0
输出: true

示例2:
输入: nums = [2,5,6,0,0,1,2], target = 3
输出: false

进阶:
这是 搜索旋转排序数组的延伸题目，本题中的nums 可能包含重复元素。
这会影响到程序的时间复杂度吗？会有怎样的影响，为什么？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    # 方法一，暴力法，44ms，43.25%
    def search(self, nums: List[int], target: int) -> bool:
        return True if target in nums else False

    # 方法二，暴力法，40ms，68.93%
    def search(self, nums: List[int], target: int) -> bool:
        for num in nums:
            if num == target:
                return True
        return False

    # 方法三，二分，44ms，43%
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            # mid 在左边有序部分
            if nums[mid] > nums[left]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # mid 在右边有序部分
            elif nums[mid] < nums[left]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            # 不确定在左边有序部分还是右边有序部分
            else:
                left += 1

        return False


if __name__ == '__main__':
    s = Solution()
    print(s.search(nums=[2, 5, 6, 0, 0, 1, 2], target=0))
    print(s.search(nums=[2, 5, 6, 0, 0, 1, 2], target=3))
    # 单元素数组
    print(s.search([1], 0))
    print(s.search([1], 1))
    print(s.search([1, 0, 1, 1, 1], 0))
