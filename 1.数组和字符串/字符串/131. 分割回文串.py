"""
给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。
回文串 是正着读和反着读都一样的字符串。

示例 1：
输入：s = "aab"
输出：[["a","a","b"],["aa","b"]]
示例 2：
输入：s = "a"
输出：[["a"]]
提示：
1 <= s.length <= 16
s 仅由小写英文字母组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-partitioning
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from functools import cache
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)

        ret = list()
        ans = list()

        @cache
        def isPalindrome(i: int, j: int) -> int:
            if i >= j:
                return 1
            return isPalindrome(i + 1, j - 1) if s[i] == s[j] else -1

        def dfs(i: int):
            if i == n:
                ret.append(ans[:])
                return

            for j in range(i, n):
                if isPalindrome(i, j) == 1:
                    ans.append(s[i:j + 1])
                    dfs(j + 1)
                    ans.pop()

        dfs(0)
        isPalindrome.cache_clear()
        return ret


if __name__ == '__main__':
    s = Solution()
    print(s.partition(s="aba"))
