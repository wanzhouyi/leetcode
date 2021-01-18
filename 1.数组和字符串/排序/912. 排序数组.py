"""
给你一个整数数组nums，请你将该数组升序排列。

示例 1：
输入：nums = [5,2,3,1]
输出：[1,2,3,5]

示例 2：
输入：nums = [5,1,1,2,0,0]
输出：[0,0,1,1,2,5]

提示：

1 <= nums.length <= 50000
-50000 <= nums[i] <= 50000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    # 方法一，系统函数，52 ms，97.02%
    def sortArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        return nums

    # 方法二，系统函数，48 ms，98.44%
    def sortArray(self, nums: List[int]) -> List[int]:
        return sorted(nums)

    # 方法三，归并排序，388 ms，10.16%
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(nums1, nums2):
            result = []
            while nums1 and nums2:
                if nums1[0] > nums2[0]:
                    result.append(nums2.pop(0))
                else:
                    result.append(nums1.pop(0))
            if nums1:
                result.extend(nums1)
            if nums2:
                result.extend(nums2)
            return result

        n = len(nums)
        if n == 0:
            return []
        elif n == 1:
            return nums
        else:
            mid = n // 2
            return merge(self.sortArray(nums[:mid]), self.sortArray(nums[mid:]))

    # 方法四，快速排序，188 ms，67.77%
    def sortArray(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        pivot = nums[0]
        left, right = [], []
        counter = 1
        for num in nums[1:]:
            if num < pivot:
                left.append(num)
            elif num > pivot:
                right.append(num)
            elif num == pivot:
                counter += 1
        return self.sortArray(left) + [pivot] * counter + self.sortArray(right)


if __name__ == '__main__':
    s = Solution()
    print(s.sortArray(nums=[5, 2, 3, 1]))
