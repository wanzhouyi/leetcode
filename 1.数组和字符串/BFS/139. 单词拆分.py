"""
给定一个非空字符串 s 和一个包含非空单词的列表 wordDict，判定s 是否可以被空格拆分为一个或多个在字典中出现的单词。
说明：
拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
示例 1：
输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
示例 2：
输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
    注意你可以重复使用字典中的单词。
示例 3：
输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-break
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    # BFS，85.32%
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dic = dict()
        for i in range(n):
            dic[i] = list(filter(lambda x: s[i:].startswith(x), wordDict))
        print(dic)
        stack = {0}
        visited = set()
        while stack:
            temp_start = stack.pop()
            if temp_start == n:
                return True
            visited.add(temp_start)
            for word in dic[temp_start]:
                new_start = temp_start + len(word)
                if new_start not in visited:
                    stack.add(new_start)
        return False


# 其它解

class Solution:
    """
    方法一：动态规划
    |""  |   l   |   e   |   e   |   t   |   c   |   o   |   d   |   e   |
    |true| false | false | false | true  | false | false | false | true  |

    初始化 dp=[False,⋯,False]，长度为 n+1。n 为字符串长度。
    dp[i] 表示 s 的前 i 位是否可以用 wordDict 中的单词表示。

    初始化 dp[0]=True，空字符可以被表示。

    遍历字符串的所有子串，遍历开始索引 i，遍历区间 [0,n)：

    遍历结束索引 j，遍历区间 [i+1,n+1)：
    若 dp[i]=True 且 s[i,⋯,j) 在 wordlistwordlist 中：dp[j]=True。
    解释：dp[i]=True说明 s 的前 i位可以用 wordDict表示，则 s[i,⋯,j) 出现在 wordDict中，说明 s的前 j位可以表示。
    返回 dp[n]

    作者：wu_yan_zu
    链接：https://leetcode-cn.com/problems/word-break/solution/dong-tai-gui-hua-ji-yi-hua-hui-su-zhu-xing-jie-shi/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(n):
            for j in range(i + 1, n + 1):
                if dp[i] and (s[i:j] in wordDict):
                    dp[j] = True
        return dp[-1]


class Solution:
    """
    方法二：记忆化回溯
    使用记忆化函数，保存出现过的 backtrack(s) ，避免重复计算。
    定义回溯函数 backtrack(s)
        若 s 长度为 0，则返回 True，表示已经使用 wordDict 中的单词分割完。
        初试化当前字符串是否可以被分割 res=False
        遍历结束索引 i，遍历区间 [1,n+1)：
        若 s[0,⋯,i−1] 在 wordDict中：res=backtrack(s[i,⋯,n−1]) or res。
        解释：保存遍历结束索引中，可以使字符串切割完成的情况。
        返回 res
    返回 backtrack(s)

    作者：wu_yan_zu
    链接：https://leetcode-cn.com/problems/word-break/solution/dong-tai-gui-hua-ji-yi-hua-hui-su-zhu-xing-jie-shi/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        import functools
        @functools.lru_cache(None)
        def back_track(s):
            if (not s):
                return True
            res = False
            for i in range(1, len(s) + 1):
                if (s[:i] in wordDict):
                    res = back_track(s[i:]) or res
            return res

        return back_track(s)


if __name__ == '__main__':
    s = Solution()
    print(s.wordBreak(s="leetcode", wordDict=["leet", "code"]))
    print(s.wordBreak(s="applepenapple", wordDict=["apple", "pen"]))
    print(s.wordBreak(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"]))
    print(s.wordBreak(
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
        , ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa",
           "aaaaaaaaaa"]))
