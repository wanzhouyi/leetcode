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
