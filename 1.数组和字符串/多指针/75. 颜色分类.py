"""
给定一个包含红色、白色和蓝色，一共n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
此题中，我们使用整数 0、1 和 2 分别表示红色、白色和蓝色。

示例 1：
输入：nums = [2,0,2,1,1,0]
输出：[0,0,1,1,2,2]

示例 2：
输入：nums = [2,0,1]
输出：[0,1,2]

示例 3：
输入：nums = [0]
输出：[0]

示例 4：
输入：nums = [1]
输出：[1]

提示：

n == nums.length
1 <= n <= 300
nums[i] 为 0、1 或 2

进阶：

你可以不使用代码库中的排序函数来解决这道题吗？
你能想出一个仅使用常数空间的一趟扫描算法吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-colors
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    # 方法一，系统函数，44 ms，32%
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()

    # 方法二，计数，36 ms，81%
    def sortColors(self, nums: List[int]) -> None:
        ct0, ct1, ct2 = nums.count(0), nums.count(1), nums.count(2)
        nums[:ct0] = [0] * ct0
        nums[ct0:ct0 + ct1] = [1] * ct1
        nums[ct0 + ct1:] = [2] * ct2

    # 方法三，双指针，48 ms，14%
    def sortColors(self, nums: List[int]) -> None:
        ptr = 0
        for idx, num in enumerate(nums):
            if num == 0:
                nums[ptr], nums[idx] = nums[idx], nums[ptr]
                ptr += 1
        for idx, num in enumerate(nums):
            if num == 1:
                nums[ptr], nums[idx] = nums[idx], nums[ptr]
                ptr += 1
