"""
升序排列的整数数组 nums 在预先未知的某个点上进行了旋转（例如， [0,1,2,4,5,6,7] 经旋转后可能变为[4,5,6,7,0,1,2] ）。
请你在数组中搜索target ，如果数组中存在这个目标值，则返回它的索引，否则返回-1。

示例 1：
输入：nums = [4,5,6,7,0,1,2], target = 0
输出：4

示例2：
输入：nums = [4,5,6,7,0,1,2], target = 3
输出：-1

示例 3：
输入：nums = [1], target = 0
输出：-1
提示：

1 <= nums.length <= 5000
-10^4 <= nums[i] <= 10^4
nums 中的每个值都 独一无二
nums 肯定会在某个点上旋转
-10^4 <= target <= 10^4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-in-rotated-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:

    # 方法一，暴力法，32 ms，94.20%
    def search(self, nums: List[int], target: int) -> int:
        def search(left, right) -> int:
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left += 1
            return -1

        # 先找到旋转点
        splitor = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                splitor = i - 1
                break
        # 分别搜索左右数组
        left_result = search(0, splitor)
        if left_result != -1:
            return left_result
        right_result = search(splitor + 1, len(nums) - 1)
        return right_result

    # 方法二，官解
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[len(nums) - 1]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.search(nums=[4, 5, 6, 7, 0, 1, 2], target=0))
    print(s.search(nums=[4, 5, 6, 7, 0, 1, 2], target=3))
    print(s.search(nums=[4, 5, 6, 7, 0, 1, 2], target=-2))
    print(s.search(nums=[4, 5, 6, 7, 0, 1, 2], target=18))
    print(s.search(nums=[1], target=0))
    print(s.search(nums=[1], target=1))
    print(s.search(nums=[1], target=2))
