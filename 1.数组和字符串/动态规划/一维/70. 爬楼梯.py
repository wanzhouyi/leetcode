"""
假设你正在爬楼梯。需要 n阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
注意：给定 n 是一个正整数。

示例 1：
输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶

示例 2：
输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/climbing-stairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    # 从上到下，48ms，10.16%
    def climbStairs(self, n: int) -> int:
        memo = {0: 1, 1: 1}

        def dp(m):
            if m in memo.keys():
                return memo[m]
            memo[m] = dp(m - 1) + dp(m - 2)
            return memo[m]

        return dp(n)

    # 从下到上，48 ms，10.16%
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        memo = {0: 1, 1: 1}
        for i in range(2, n + 1):
            memo[i] = memo[i - 1] + memo[i - 2]
        return memo[n]

    # 从下到上（状态压缩），32 ms，92.06%
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        pre, last = 1, 1
        for i in range(2, n + 1):
            pre, last = last, pre + last
        return last


if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs(2))
    print(s.climbStairs(3))
    # 0级和1级
    print(s.climbStairs(0))
    print(s.climbStairs(1))
    # 4级
    print(s.climbStairs(4))
