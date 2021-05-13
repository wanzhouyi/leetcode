"""
有一个长度为arrLen的数组，开始有一个指针在索引0 处。
每一步操作中，你可以将指针向左或向右移动 1 步，或者停在原地（指针不能被移动到数组范围外）。
给你两个整数steps 和arrLen ，请你计算并返回：在恰好执行steps次操作以后，指针仍然指向索引0 处的方案数。
由于答案可能会很大，请返回方案数 模10^9 + 7 后的结果。

示例 1：
输入：steps = 3, arrLen = 2
输出：4
解释：3 步后，总共有 4 种不同的方法可以停在索引 0 处。
向右，向左，不动
不动，向右，向左
向右，不动，向左
不动，不动，不动

示例 2：
输入：steps = 2, arrLen = 4
输出：2
解释：2 步后，总共有 2 种不同的方法可以停在索引 0 处。
向右，向左
不动，不动

示例 3：
输入：steps = 4, arrLen = 2
输出：8

提示：
1 <= steps <= 500
1 <= arrLen<= 10^6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        """
        暴力解法，超时
        """
        ans = 0

        def dfs(last_steps, current_pos):
            if last_steps < 0:
                return
            if last_steps == 0 and current_pos == 0:
                nonlocal ans
                ans += 1
                return

            if current_pos - 1 >= 0:
                dfs(last_steps - 1, current_pos - 1)

            dfs(last_steps - 1, current_pos)

            if current_pos + 1 < arrLen:
                dfs(last_steps - 1, current_pos + 1)

        dfs(steps, 0)

        return ans

    def numWays(self, steps: int, arrLen: int) -> int:
        """
        定义 f[i][j] 代表当前剩余操作数为 i，所在位置为 j 的所有方案数。

        起始位置为 0，操作次数为 step，即有初始化条件 f[step][0]=1，f[0][0] 则是我们的最终答案。

        不失一般性的考虑 f[i][j] 可以由哪些状态转移而来：

        由「原地」操作到达当前状态，消耗一次操作，此时由状态 f[i + 1][j] 转移而来
        由「向左」操作到达当前状态，消耗一次操作，此时由状态 f[i + 1][j + 1] 转移而来
        由「向右」操作到达当前状态，消耗一次操作，此时由状态 f[i + 1][j - 1] 转移而来
        求的是方案数，即最终的 f[i][j]为三者累加值。

        同时我们发现 f[i][x]依赖于 f[i + 1][y]，因此我们需要按照「step从大到小」的顺序进行转移。

        同时我们根据「最终回到下标 0 位置」可以推断出，最远到达的位置为 step / 2（再远就回不来了）。
        将最远到达位置与数组最大下标取 min 即可确定维度 step的范围。

        作者：AC_OIer
        链接：https://leetcode-cn.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/solution/gong-shui-san-xie-xiang-jie-xian-xing-dp-m9q9/
        来源：力扣（LeetCode）
        著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        """

        MOD = 10 ** 9 + 7
        # 如果想要取到steps/2那一位, 需要+1, 但是arrLen不需要+1, 本来 arrLen = 2, 数组下标可以从 0 开始的
        maxLen = min(steps // 2 + 1, arrLen)
        # 不能使用这个来初始化数组! 会导致数组中的子一维数组地址都是一样, 改动一个其他都会改变
        # dp = [[0] * maxLen] * (steps + 1)
        dp = [[0 for _ in range(maxLen)] for _ in range(steps + 1)]

        # 移动0 step 到 0 这个arrLen只有1种途径: 不移动
        dp[0][0] = 1
        # 这里 step 从 1 开始是因为 移动 0 步到任意的arrLen都没有用, 过不去...
        for step in range(1, steps + 1):
            for j in range(maxLen):
                # 不移动
                dp[step][j] = dp[step - 1][j] % MOD

                # 从 j-1 那格到 j, 右移一步
                if j - 1 >= 0:
                    dp[step][j] = (dp[step][j] + dp[step - 1][j - 1]) % MOD
                # 从j+1 那格到 j, 左移一步
                if j + 1 < maxLen:
                    dp[step][j] = (dp[step][j] + dp[step - 1][j + 1]) % MOD
        # 最终要的结果是在 steps 步, 且回到原点 0的方案数
        return dp[steps][0]


if __name__ == '__main__':
    s = Solution()
    # print(s.numWays(steps=3, arrLen=2))  # 4
    # print(s.numWays(steps=2, arrLen=4))  # 2
    # print(s.numWays(steps=4, arrLen=2)) #8
    # print(s.numWays(steps=500,arrLen=10**6))

    print(s.numWays(steps=1, arrLen=500))
    print(s.numWays(steps=2, arrLen=500))
    print(s.numWays(steps=3, arrLen=500))
    print(s.numWays(steps=4, arrLen=500))
    print(s.numWays(steps=5, arrLen=500))
    print(s.numWays(steps=6, arrLen=500))
