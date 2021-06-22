"""
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回-1。

你可以认为每种硬币的数量是无限的。



示例1：

输入：coins = [1, 2, 5], amount = 11
输出：3 
解释：11 = 5 + 5 + 1
示例 2：

输入：coins = [2], amount = 3
输出：-1
示例 3：

输入：coins = [1], amount = 0
输出：0
示例 4：

输入：coins = [1], amount = 1
输出：1
示例 5：

输入：coins = [1], amount = 2
输出：2


提示：

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/coin-change
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import functools
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[float('inf')] * (len(coins)) for _ in range(amount + 1)]
        for i in range(len(coins)):
            dp[0][i] = 0
        for x in range(1, amount + 1):
            for y in range(len(coins)):
                if x - coins[y] >= 0:
                    dp[x][y] = min(dp[x - coins[y]]) + 1
        # print(dp)
        mn = min(dp[-1])
        return mn if mn < float('inf') else -1


class Solution:
    """
    方法一：记忆化搜索
    我们能改进上面的指数时间复杂度的解吗？当然可以，利用动态规划，我们可以在多项式的时间范围内求解。首先，我们定义：

    F(S)：组成金额 S 所需的最少硬币数量
    [c_0…c_{n−1}] ：可选的 n 枚硬币面额值

    我们注意到这个问题有一个最优的子结构性质，这是解决动态规划问题的关键。最优解可以从其子问题的最优解构造出来。
    如何将问题分解成子问题？假设我们知道 F(S) ，即组成金额 S 最少的硬币数，最后一枚硬币的面值是 C。
    那么由于问题的最优子结构，转移方程应为：
    F(S) = F(S - C) + 1
    但我们不知道最后一枚硬币的面值是多少，所以我们需要枚举每个硬币面额值 c_0, c_1, c_2 ……c_{n -1}
    并选择其中的最小值。下列递推关系成立：

    F(S) = min{i=0 ... n-1}F(S - c_i) } + 1 \ \text{subject to} \ \ S-c_i \geq 0
    F(S)=
    i=0...n−1
    min
    ​
     F(S−c
    i
    ​
     )+1subjecttoS−c
    i
    ​
     ≥0

    F(S)=0,when S=0
    F(S)=−1,when n=0



    在上面的递归树中，我们可以看到许多子问题被多次计算。例如， F(1)F(1) 被计算了 1313 次。为了避免重复的计算，我们将每个子问题的答案存在一个数组中进行记忆化，如果下次还要计算这个问题的值直接从数组中取出返回即可，这样能保证每个子问题最多只被计算一次。

    作者：LeetCode-Solution
    链接：https://leetcode-cn.com/problems/coin-change/solution/322-ling-qian-dui-huan-by-leetcode-solution/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def coinChange(self, coins: List[int], amount: int) -> int:
        @functools.lru_cache(amount)
        def dp(rem) -> int:
            if rem < 0: return -1
            if rem == 0: return 0
            mini = int(1e9)
            for coin in self.coins:
                res = dp(rem - coin)
                if res >= 0 and res < mini:
                    mini = res + 1
            return mini if mini < int(1e9) else -1

        self.coins = coins
        if amount < 1: return 0
        return dp(amount)


class Solution:
    """自下而上"""

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1
