"""
给你一个包含 n 个整数的数组nums，判断nums中是否存在三个元素 a，b，c ，使得a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。
注意：答案中不可以包含重复的三元组。

示例 1：
输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]

示例 2：
输入：nums = []
输出：[]

示例 3：
输入：nums = [0]
输出：[]

提示：

0 <= nums.length <= 3000
-105 <= nums[i] <= 105

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        nums.sort()
        n = len(nums) - 1
        result = set()
        for idx, num in enumerate(nums):
            left, right = idx + 1, n
            while left < right:
                sm = nums[left] + nums[right] + num
                if sm == 0:
                    result.add((num, nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif sm > 0:
                    right -= 1
                elif sm < 0:
                    left += 1
        return [list(x) for x in result]


class Solution:
    """
    排序 + 双指针
    本题的难点在于如何去除重复解。

    算法流程：
    特判，对于数组长度 nn，如果数组为 null 或者数组长度小于 3，返回 []。
    对数组进行排序。
    遍历排序后数组：
    若 nums[i]>0：因为已经排序好，所以后面不可能有三个数加和等于 0，直接返回结果。
    对于重复元素：跳过，避免出现重复解
    令左指针 L=i+1，右指针 R=n−1，当 L<R 时，执行循环：
    当 nums[i]+nums[L]+nums[R]==0，执行循环，判断左界和右界是否和下一位置重复，去除重复解。
    并同时将 L,R移到下一位置，寻找新的解
    若和大于 0，说明 nums[R] 太大，R 左移
    若和小于 0，说明 nums[L] 太小，L 右移

    作者：wu_yan_zu
    链接：https://leetcode-cn.com/problems/3sum/solution/pai-xu-shuang-zhi-zhen-zhu-xing-jie-shi-python3-by/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def threeSum(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        res = []
        if (not nums or n < 3):
            return []
        nums.sort()
        res = []
        for i in range(n):
            if (nums[i] > 0):
                return res
            if (i > 0 and nums[i] == nums[i - 1]):
                continue
            L = i + 1
            R = n - 1
            while (L < R):
                if (nums[i] + nums[L] + nums[R] == 0):
                    res.append([nums[i], nums[L], nums[R]])
                    while (L < R and nums[L] == nums[L + 1]):
                        L = L + 1
                    while (L < R and nums[R] == nums[R - 1]):
                        R = R - 1
                    L = L + 1
                    R = R - 1
                elif (nums[i] + nums[L] + nums[R] > 0):
                    R = R - 1
                else:
                    L = L + 1
        return res
