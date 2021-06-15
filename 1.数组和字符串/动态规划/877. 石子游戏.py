"""
亚历克斯和李用几堆石子在做游戏。偶数堆石子排成一行，每堆都有正整数颗石子piles[i]。

游戏以谁手中的石子最多来决出胜负。石子的总数是奇数，所以没有平局。

亚历克斯和李轮流进行，亚历克斯先开始。 每回合，玩家从行的开始或结束处取走整堆石头。 这种情况一直持续到没有更多的石子堆为止，此时手中石子最多的玩家获胜。

假设亚历克斯和李都发挥出最佳水平，当亚历克斯赢得比赛时返回true，当李赢得比赛时返回false。



示例：

输入：[5,3,4,5]
输出：true
解释：
亚历克斯先开始，只能拿前 5 颗或后 5 颗石子 。
假设他取了前 5 颗，这一行就变成了 [3,4,5] 。
如果李拿走前 3 颗，那么剩下的是 [4,5]，亚历克斯拿走后 5 颗赢得 10 分。
如果李拿走后 5 颗，那么剩下的是 [3,4]，亚历克斯拿走后 4 颗赢得 9 分。
这表明，取前 5 颗石子对亚历克斯来说是一个胜利的举动，所以我们返回 true 。


提示：

2 <= piles.length <= 500
piles.length 是偶数。
1 <= piles[i] <= 500
sum(piles)是奇数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/stone-game
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        ans = [0] * (n + 1)
        for idx in range(n):
            if idx % 2 == 0:
                ans[idx + 1] = ans[idx] + piles[idx]
            else:
                ans[idx + 1] = max(ans[idx], ans[idx - 1] + piles[idx])
        if ans[-1] * 2 > sum(piles):
            return True
        return False

    ########以下是题解
    def stoneGame(self, nums):
        """
        递归大法：
        如果我们先选了左边 对手一定会选择一个让我们总和最小的数
        如果我们选了右边，对手也一定会选择一个让我们总和最小的数
        """
        d = {}

        def mefirst(i, j):
            # 记忆化
            if (i, j) in d: return d[(i, j)]
            # 左指针不能大于右指针
            if i > j: return 0

            if i == j: return nums[i]

            # chooseleft: 如果我们先选了左边 对手一定会选择一个让我们总和最小的数
            chooseleft = nums[i] + min(mefirst(i + 2, j), mefirst(i + 1, j - 1))

            # 同理 如果我们选了右边，对手也一定会选择一个让我们总和最小的数
            chooseright = nums[j] + min(mefirst(i + 1, j - 1), mefirst(i, j - 2))

            # 取这两者最大值
            score = max(chooseleft, chooseright)

            # 记录结果
            d[(i, j)] = score
            return score

        # 我方能得到的最大分数
        me = mefirst(0, len(nums) - 1)

        # 看我方能得到的最大分数是否超过对方能得到的最大分数
        return me >= sum(nums) - me

    def stoneGame(self, piles: List[int]) -> bool:
        """
        定义二维数组dp，其行数和列数都等于石子的堆数，dp[i][j]表示当剩下的石子堆为下标 i 到下标 j 时，
        当前玩家与另一个玩家的石子数量之差的最大值，注意当前玩家不一定是先手Alex。
        只有当i≤j 时，剩下的石子堆才有意义，因此当 i>j 时，dp[i][j]=0。
        当 i=j 时，只剩下一堆石子，当前玩家只能取走这堆石子，因此对于所有0≤i<nums.length，都有dp[i][i]=piles[i]。
        当 i<j 时，当前玩家可以选择取走 piles[i] 或 piles[j]，然后轮到另一个玩家在剩下的石子堆中取走石子。
        在两种方案中，当前玩家会选择最优的方案，使得自己的石子数量最大化。因此可以得到如下状态转移方程：

        dp[i][j]=max(piles[i]−dp[i+1][j],piles[j]−dp[i][j−1])

        最后判断 dp[0][piles.length−1] 的值，如果大于 0，则 Alex 的石子数量大于Lee 的石子数量，因此 Alex 赢得比赛，否则 Lee 赢得比赛。

        作者：LeetCode-Solution
        链接：https://leetcode-cn.com/problems/stone-game/solution/shi-zi-you-xi-by-leetcode-solution/
        来源：力扣（LeetCode）
        著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        """
        length = len(piles)
        dp = [[0] * length for _ in range(length)]
        for i, pile in enumerate(piles):
            dp[i][i] = pile
        for i in range(length - 2, -1, -1):
            for j in range(i + 1, length):
                dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1])
        return dp[0][length - 1] > 0

        """
        上述代码中使用了二维数组dp。分析状态转移方程可以看到，dp[i][j] 的值只和dp[i+1][j] 与 dp[i][j−1] 有关，
        即在计算dp 的第 i 行的值时，只需要使用到dp 的第 i 行和第 i+1 行的值，因此可以使用一维数组代替二维数组，对空间进行优化。
        """

        def stoneGame(self, piles: List[int]) -> bool:
            length = len(piles)
            dp = [0] * length
            for i, pile in enumerate(piles):
                dp[i] = pile
            for i in range(length - 2, -1, -1):
                for j in range(i + 1, length):
                    dp[j] = max(piles[i] - dp[j], piles[j] - dp[j - 1])
            return dp[length - 1] > 0


if __name__ == '__main__':
    s = Solution()
    print(s.stoneGame([5, 3, 4, 5]))
