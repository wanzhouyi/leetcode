"""
给定一个字符串s和一个非空字符串p，找到s中所有是p的字母异位词的子串，返回这些子串的起始索引。

字符串只包含小写英文字母，并且字符串s和 p的长度都不超过 20100。

说明：

字母异位词指字母相同，但排列不同的字符串。
不考虑答案输出的顺序。
示例1:

输入:
s: "cbaebabacd" p: "abc"

输出:
[0, 6]

解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。
示例 2:

输入:
s: "abab" p: "ab"

输出:
[0, 1, 2]

解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的字母异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的字母异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的字母异位词。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-all-anagrams-in-a-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    # 滑动窗口，效率很差
    def findAnagrams(self, s: str, p: str) -> List[int]:
        lenp = len(p)
        sortedp = sorted(p)
        ans = []
        for r in range(lenp, len(s) + 1):
            if sorted(s[r - lenp:r]) == sortedp:
                ans.append(r - lenp)
        return ans

    # 官解，计数
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_count = [0] * 26
        s_count = [0] * 26
        left = 0;
        res = []
        for c in p:
            p_count[(ord(c) - 97)] += 1
        for right in range(len(s)):
            if right < len(p) - 1:
                s_count[ord(s[right]) - 97] += 1
                continue
            s_count[ord(s[right]) - 97] += 1
            if p_count == s_count:
                res.append(left)
            s_count[ord(s[left]) - 97] -= 1
            left += 1
        return res
