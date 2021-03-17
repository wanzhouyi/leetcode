"""
给定一个字符串 s 和一个字符串 t ，计算在 s 的子序列中 t 出现的个数。
字符串的一个 子序列 是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。
（例如，"ACE"是"ABCDE"的一个子序列，而"AEC"不是）
题目数据保证答案符合 32 位带符号整数范围。

示例1：
输入：s = "rabbbit", t = "rabbit"
输出：3
解释：
如下图所示, 有 3 种可以从 s 中得到 "rabbit" 的方案。
(上箭头符号 ^ 表示选取的字母)
rabbbit
^^^^ ^^
rabbbit
^^ ^^^^
rabbbit
^^^ ^^^

示例2：
输入：s = "babgbag", t = "bag"
输出：5
解释：
如下图所示, 有 5 种可以从 s 中得到 "bag" 的方案。 
(上箭头符号 ^ 表示选取的字母)
babgbag
^^ ^
babgbag
^^    ^
babgbag
^    ^^
babgbag
  ^  ^^
babgbag
    ^^^

提示：

0 <= s.length, t.length <= 1000
s 和 t 由英文字母组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/distinct-subsequences
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """
        假设我们有字符串 s = abcc 和 字符串 abc
        设定dp[i][j]为使用s的前i个字符能够最多组成多少个t的前j个字符
        当s[j] == t[i] 时：此时假设j=3，i=2，需要比较的是 abcc 中含有多少个abc
            1.当考虑使用第i个元素时，即我们让 abcc 中的最后一个c 和abc最后一个c匹配上，
            这时我们需要看的是 abc中含有多少个 ab ,对应dp[i-1][j-1]
            2.当不考虑使用第i个元素时，我们需要看的是 abc 中含有多少个abc ,对应dp[i][j-1]

        转移方程为dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
        当s[j] ！= t[i] 时，此时假设j=3，i=2
        只有一种情况，只需要看的是 abc 中含有多少个abc即可，对应dp[i][j-1]
        转移方程为dp[i][j] = dp[i][j-1]
        作者：xiao-xue-66
        链接：https://leetcode-cn.com/problems/distinct-subsequences/solution/pythonti-jie-yi-kan-jiu-dong-de-fen-xi-yao-yao-yao/
        来源：力扣（LeetCode）
        著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        """

        dp = [[0] * (len(s) + 1) for _ in range(len(t) + 1)]

        for i in range(len(s) + 1):
            dp[0][i] = 1

        for i in range(1, len(t) + 1):
            for j in range(1, len(s) + 1):
                if t[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]

        return dp[-1][-1]
