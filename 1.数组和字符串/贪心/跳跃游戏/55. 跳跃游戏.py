"""
给定一个非负整数数组nums ，你最初位于数组的 第一个下标 。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
判断你是否能够到达最后一个下标。

示例1：
输入：nums = [2,3,1,1,4]
输出：true
解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。

示例2：
输入：nums = [3,2,1,0,4]
输出：false
解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。

提示：
1 <= nums.length <= 3 * 10^4
0 <= nums[i] <= 10^5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/jump-game
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_pos = 0
        end = 0
        for i in range(len(nums)):
            if max_pos >= i:
                max_pos = max(max_pos, nums[i] + i)
                if end == i:
                    end = max_pos
        if end < len(nums) - 1:
            return False
        return True


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n, rightmost = len(nums), 0
        for i in range(n):
            if i <= rightmost:
                rightmost = max(rightmost, i + nums[i])
                if rightmost >= n - 1:
                    return True
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.canJump(nums=[2, 3, 1, 1, 4]))
    print(s.canJump(nums=[3, 2, 1, 0, 4]))
