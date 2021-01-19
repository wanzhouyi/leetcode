"""
给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。

示例 1:

输入: [1,2,3]
输出: 6
示例 2:

输入: [1,2,3,4]
输出: 24
注意:

给定的整型数组长度范围是[3,104]，数组中所有的元素范围是[-1000, 1000]。
输入的数组中任意三个数的乘积不会超出32位有符号整数的范围。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-product-of-three-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    # 方法一，暴力解，56 ms，99.76%
    def maximumProduct(self, nums: List[int]) -> int:
        import bisect
        nums.sort()
        zero_position = bisect.bisect_left(nums, 0)
        # print(zero_position)
        if zero_position == 0 or zero_position == 1 or zero_position == len(nums):
            # 全为正数,仅有一个负数的情况,全为负数的情况
            return nums[-1] * nums[-2] * nums[-3]
        else:
            j1 = nums[0] * nums[1] * nums[-1]  # 选两个
            j2 = nums[-1] * nums[-2] * nums[-3]  # 不选
            return max(j1, j2)


if __name__ == '__main__':
    s = Solution()
    print(s.maximumProduct([1, 2, 3]))  # 6
    print(s.maximumProduct([1, 2, 3, 4]))  # 24
    print(s.maximumProduct([-9, 1, 2, 3, 4]))  # 24
    print(s.maximumProduct([-5, -4, -3, -2]))  # -24

    print(s.maximumProduct([-9, -8, 2]))  # 144
    print(s.maximumProduct([-9, -8, 1, 2, 3, 4]))  # 288
    print(s.maximumProduct([-9, -8, 1, 2, 9, 10]))  # 720
    print(s.maximumProduct([-9, -8, -7, 1, 2, 3, 4]))  # 288
