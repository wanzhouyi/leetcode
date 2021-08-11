"""
给你一个字符串 s ，找出其中最长的回文子序列，并返回该序列的长度。
子序列定义为：不改变剩余字符顺序的情况下，删除某些字符或者不删除任何字符形成的一个序列。

示例 1：

输入：s = "bbbab"
输出：4
解释：一个可能的最长回文子序列为 "bbbb" 。
示例 2：

输入：s = "cbbd"
输出：2
解释：一个可能的最长回文子序列为 "bb" 。

提示：

1 <= s.length <= 1000
s 仅由小写英文字母组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    """
    方法一：动态规划
    对于一个子序列而言，如果它是回文子序列，并且长度大于 2，那么将它首尾的两个字符去除之后，它仍然是个回文子序列。
    因此可以用动态规划的方法计算给定字符串的最长回文子序列。

    用 dp[i][j] 表示字符串 s 的下标范围 [i, j] 内的最长回文子序列的长度。
    假设字符串 s 的长度为 n，则只有当 0≤i≤j<n 时，才会有 dp[i][j]>0，否则dp[i][j]=0。

    由于任何长度为 1的子序列都是回文子序列，因此动态规划的边界情况是，对任意 0≤i<n，都有dp[i][i]=1。

    当 i < j 时，计算 dp[i][j] 需要分别考虑 s[i] 和 s[j] 相等和不相等的情况：

    如果 s[i] = s[j]，则首先得到 s 的下标范围 [i+1, j-1] 内的最长回文子序列，
    然后在该子序列的首尾分别添加 s[i] 和 s[j]，即可得到 s 的下标范围 [i, j]内的最长回文子序列，
    因此 dp[i][j]=dp[i+1][j−1]+2；

    如果 s[i] =s[j]，则 s[i] 和 s[j] 不可能同时作为同一个回文子序列的首尾，因此 dp[i][j]=max(dp[i+1][j],dp[i][j−1])。

    由于状态转移方程都是从长度较短的子序列向长度较长的子序列转移，因此需要注意动态规划的循环顺序。

    最终得到 dp[0][n−1] 即为字符串 s 的最长回文子序列的长度。

    作者：LeetCode-Solution
    链接：https://leetcode-cn.com/problems/longest-palindromic-subsequence/solution/zui-chang-hui-wen-zi-xu-lie-by-leetcode-hcjqp/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][n - 1]


if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindromeSubseq(s="bbbab"))
