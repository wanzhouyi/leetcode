"""
如果一个数列 至少有三个元素 ，并且任意两个相邻元素之差相同，则称该数列为等差数列。

例如，[1,3,5,7,9]、[7,7,7,7] 和 [3,-1,-5,-9] 都是等差数列。
给你一个整数数组 nums ，返回数组 nums 中所有为等差数组的 子数组 个数。

子数组 是数组中的一个连续序列。



示例 1：

输入：nums = [1,2,3,4]
输出：3
解释：nums 中有三个子等差数组：[1, 2, 3]、[2, 3, 4] 和 [1,2,3,4] 自身。
示例 2：

输入：nums = [1]
输出：0


提示：

1 <= nums.length <= 5000
-1000 <= nums[i] <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/arithmetic-slices
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0

        def cal(n):
            if n < 3:
                return 0
            sm = 0
            for i in range(3, n + 1):
                sm += (n - i + 1)
            return sm

        cha = float('inf')
        ans = 0
        left = 0
        for right in range(1, n):
            if nums[right] - nums[right - 1] != cha:
                cha = nums[right] - nums[right - 1]
                if right - left + 1 >= 3:
                    ans += cal(right - left + 1)
                left = right
        ans += cal(right - left + 2)
        return ans

    def numberOfArithmeticSlices1(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        cha_arr = [nums[i] - nums[i - 1] for i in range(1, len(nums))]

        def cal(n):
            if n < 3:
                return 0
            sm = 0
            for i in range(3, n + 1):
                sm += (n - i + 1)
            return sm

        n = len(cha_arr)
        ans = 0
        left = 0
        for right in range(n):
            if cha_arr[right] != cha_arr[left]:
                if right - left >= 2:
                    ans += cal(right - left + 1)
                left = right
        ans += cal(right - left + 2)
        return ans


if __name__ == '__main__':
    s = Solution()
    # print(s.numberOfArithmeticSlices(nums=[1, 2, 3, 4]))
    # print(s.numberOfArithmeticSlices(nums=[1, 2, 3, 4, 7]))
    # print(s.numberOfArithmeticSlices(nums=[99, 1, 2, 3, 4, 7]))
    # print(s.numberOfArithmeticSlices(nums=[1, 2, 3]))
    # print(s.numberOfArithmeticSlices(nums=[3, 2, 1]))
    # print(s.numberOfArithmeticSlices(nums=[1, 2]))
    # print(s.numberOfArithmeticSlices(nums=[1]))
    # print(s.numberOfArithmeticSlices([1, 3, 5, 7, 9]))
    # print(s.numberOfArithmeticSlices([7, 7, 7, 7]))
    # print(s.numberOfArithmeticSlices([3, -1, -5, -9]))
    print(s.numberOfArithmeticSlices([1, 2, 3, 8, 9, 10]))
