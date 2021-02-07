"""
给你一个长度为n的整数数组，请你判断在 最多 改变1 个元素的情况下，该数组能否变成一个非递减数列。

我们是这样定义一个非递减数列的：对于数组中所有的i (0 <= i <= n-2)，总满足 nums[i] <= nums[i + 1]。



示例 1:

输入: nums = [4,2,3]
输出: true
解释: 你可以通过把第一个4变成1来使得它成为一个非递减数列。
示例 2:

输入: nums = [4,2,1]
输出: false
解释: 你不能在只改变一个元素的情况下将其变为非递减数列。


说明：

1 <= n <= 10 ^ 4
- 10 ^ 5<= nums[i] <= 10 ^ 5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/non-decreasing-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                new1 = nums[:i] + [nums[i + 1]] * 2 + nums[i + 2:]
                if sorted(new1) == new1:
                    return True
                new2 = nums[:i] + [nums[i]] * 2 + nums[i + 2:]
                if sorted(new2) == new2:
                    return True
                return False
        return True

    def checkPossibility(self, nums: List[int]) -> bool:
        changed = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if changed:
                    return False
                changed = True

                # 修改num[i]会导致nums[i-1] > nums[i]
                if i > 0 and nums[i - 1] > nums[i + 1]:
                    nums[i + 1] = nums[i]
                else:
                    nums[i] = nums[i + 1]
        return True

# if __name__ == '__main__':
#     s = Solution()
#     print(s.checkPossibility([4, 2, 3]))
#     # print(s.checkPossibility([4, 2, 1]))
#     # print(s.checkPossibility([4]))
#     # print(s.checkPossibility([4, 5, 6]))
#     print(s.checkPossibility([4, 4, 3, 3]))
#     # print(s.checkPossibility([4, 4, 3]))
#     # print(s.checkPossibility([3, 3, 3]))
#     # print(s.checkPossibility([4, 3]))
#     # print(s.checkPossibility([4, 5]))
#     print(s.checkPossibility([4, 4, 3, 8]))
#     print(s.checkPossibility([4, 4, 3]))
