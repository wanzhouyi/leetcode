"""
给定一个字符串，编写一个函数判定其是否为某个回文串的排列之一。
回文串是指正反两个方向都一样的单词或短语。排列是指字母的重新排列。
回文串不一定是字典当中的单词。

示例1：

输入："tactcoa"
输出：true（排列有"tacocat"、"atcocta"，等等）

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-permutation-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        """
        使用counter，中心点要么是一个，要么没有，所有最后剩下的要么是0，要么是1
        """
        ct = collections.Counter(s)
        ans = []
        while len(ct) > 0:
            key, val = ct.popitem()
            if val % 2 != 0:
                ans.append(key)
        return len(ans) < 2

    def canPermutePalindrome(self, s: str) -> bool:
        dic = dict()
        for char in s:
            if dic.get(char):
                dic.pop(char)
            else:
                dic[char] = 1
        return len(dic) < 2


if __name__ == '__main__':
    s = Solution()
    print(s.canPermutePalindrome("tactcoa"))
