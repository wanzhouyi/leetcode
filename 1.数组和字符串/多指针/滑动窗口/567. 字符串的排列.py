"""
给定两个字符串s1和s2，写一个函数来判断 s2 是否包含 s1的排列。
换句话说，第一个字符串的排列之一是第二个字符串的子串。

示例 1：

输入: s1 = "ab" s2 = "eidbaooo"
输出: True
解释: s2 包含 s1 的排列之一 ("ba").
示例 2：

输入: s1= "ab" s2 = "eidboaoo"
输出: False

提示：

输入的字符串只包含小写字母
两个字符串的长度都在 [1, 10,000] 之间

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutation-in-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from collections import Counter


class Solution:
    # 方法一，使用滑动窗口，95.43%
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        这里有个小技巧，Counter对象是可以通过=来确定是否相等的
        """
        ns1, ns2 = len(s1), len(s2)
        left = 0
        cts1 = Counter(s1)
        cts2 = Counter(s2[:ns1])
        if cts2 == cts1:
            return True
        for right in range(ns1, ns2):
            cts2[s2[right]] += 1
            cts2[s2[left]] -= 1
            if cts2[s2[left]] == 0:
                cts2.pop(s2[left])
            left += 1
            if cts2 == cts1:
                return True
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.checkInclusion(s1="ab", s2="eidbaooo"))
    print(s.checkInclusion(s1="ab", s2="ab"))
    print(s.checkInclusion(s1="ab", s2="eidboaoo"))
    print(s.checkInclusion('a', 'a'))
