"""
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，
影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
给定一个代表每个房屋存放金额的非负整数数组，计算你不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

示例 1：
输入：[1,2,3,1]
输出：4
解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
    偷窃到的最高金额 = 1 + 3 = 4 。

示例 2：
输入：[2,7,9,3,1]
输出：12
解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
    偷窃到的最高金额 = 2 + 9 + 1 = 12 。

提示：
0 <= nums.length <= 100
0 <= nums[i] <= 400

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/house-robber
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    # 未剪枝，会超时
    def rob(self, nums: List[int]) -> int:
        def dp(ls):
            if not ls:
                return 0
            return max(
                # 偷
                ls[0] + dp(ls[2:]),
                # 不偷
                dp(ls[1:])
            )

        return dp(nums)

    # 自下而上，36ms，78.29%
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        dp = {-1: 0, 0: nums[0]}
        for i in range(1, n):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
        return dp[n - 1]

    # 官解，36ms，78.29%
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        size = len(nums)
        if size == 1:
            return nums[0]

        dp = [0] * size
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, size):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[size - 1]


if __name__ == '__main__':
    s = Solution()
    print(s.rob([1, 2, 3, 1]))
    print(s.rob([2, 7, 9, 3, 1]))
    # 0-2个元素
    print(s.rob([]))
    print(s.rob([1]))
    print(s.rob([1, 2]))
    print(s.rob([1, 2, 3]))
    import random as r

    print(s.rob([r.randint(0, 400) for _ in range(101)]))
