"""
给定两个字符串s和 p，找到s中所有p的异位词的子串，返回这些子串的起始索引。不考虑答案输出的顺序。

异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。



示例1:

输入: s = "cbaebabacd", p = "abc"
输出: [0,6]
解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。
示例 2:

输入: s = "abab", p = "ab"
输出: [0,1,2]
解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。


提示:

1 <= s.length, p.length <= 3 * 104
s和p仅包含小写字母

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-all-anagrams-in-a-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
from sortedcontainers import SortedList


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        sp = sorted(p)
        ln = len(p)
        ans = []
        for i in range(len(s) - ln + 1):
            if sorted(s[i:i + ln]) == sp:
                ans.append(i)
        return ans


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        from collections import Counter
        ln = len(p)
        ctp = Counter(p)
        cts = Counter(s[:ln])
        ans = []
        for i in range(len(s) - ln + 1):
            if all(map(lambda x: ctp[x] == cts[x], ctp.keys())):
                ans.append(i)
            cts[s[i]] -= 1
            if i + ln <= len(s) - 1:
                cts[s[i + ln]] += 1
        return ans


class Solution:
    """
    方法一：滑动窗口
    思路
    根据题目要求，我们需要在字符串 ss 寻找字符串 pp 的异位词。因为字符串 pp 的异位词的长度一定与字符串 pp 的长度相同，所以我们可以在字符串 ss 中构造一个长度为与字符串 pp 的长度相同的滑动窗口，并在滑动中维护窗口中每种字母的数量；当窗口中每种字母的数量与字符串 pp 中每种字母的数量相同时，则说明当前窗口为字符串 pp 的异位词。
    算法
    在算法的实现中，我们可以使用数组来存储字符串 pp 和滑动窗口中每种字母的数量。
    细节
    当字符串 ss 的长度小于字符串 pp 的长度时，字符串 ss 中一定不存在字符串 pp 的异位词。但是因为字符串 ss 中无法构造长度与字符串 pp 的长度相同的窗口，所以这种情况需要单独处理。

    作者：LeetCode-Solution
    链接：https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/solution/zhao-dao-zi-fu-chuan-zhong-suo-you-zi-mu-xzin/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_len, p_len = len(s), len(p)

        if s_len < p_len:
            return []

        ans = []
        s_count = [0] * 26
        p_count = [0] * 26
        for i in range(p_len):
            s_count[ord(s[i]) - 97] += 1
            p_count[ord(p[i]) - 97] += 1

        if s_count == p_count:
            ans.append(0)

        for i in range(s_len - p_len):
            s_count[ord(s[i]) - 97] -= 1
            s_count[ord(s[i + p_len]) - 97] += 1

            if s_count == p_count:
                ans.append(i + 1)

        return ans


if __name__ == '__main__':
    s = Solution()
    # print(s.findAnagrams(s="cbaebabacd", p="abc"))
    # print(s.findAnagrams(s="abab", p="ab"))
    print(s.findAnagrams("aa", "bb"))
