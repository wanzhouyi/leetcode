"""
给定两个字符串 s1 和 s2，请编写一个程序，确定其中一个字符串的字符重新排列后，能否变成另一个字符串。
示例 1：
输入: s1 = "abc", s2 = "bca"
输出: true
示例 2：
输入: s1 = "abc", s2 = "bad"
输出: false
说明：
0 <= len(s1) <= 100
0 <= len(s2) <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/check-permutation-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        """
        方法一，40ms，通过将两个字符串排序后比较排序后的数组是否相等
        """
        if len(s1) != len(s2):
            return False
        s1_sort = sorted(s1)
        s2_sort = sorted(s2)
        for i in range(len(s1)):
            if s1_sort[i] != s2_sort[i]:
                return False
        return True

    def CheckPermutation(self, s1: str, s2: str) -> bool:
        """
        方法二，36ms，使用计数器
        """
        from collections import Counter
        ct1, ct2 = Counter(s1), Counter(s2)
        if len(ct1.items()) != len(ct2.items()):
            return False
        return all(map(lambda x: ct1[x] == ct2[x], ct1.keys()))

    def CheckPermutation(self, s1: str, s2: str) -> bool:
        """
        方法三，28ms，散列表计数器
        """
        if len(s1) != len(s2):
            return False
        ct1 = [0] * 26
        ct2 = [0] * 26
        for i in s1:
            ct1[ord(i) - 97] += 1
        for j in s2:
            ct2[ord(j) - 97] += 1

        for idx in range(26):
            if ct1[idx] != ct2[idx]:
                return False
        return True

    def CheckPermutation(self, s1: str, s2: str) -> bool:
        """
        方法三，一个加一个减，最少使用两次的循环
        """
        if len(s1) != len(s2):
            return False
        h_map = {}
        for s in s1:
            h_map.setdefault(s, 0)
            h_map[s] += 1

        for s in s2:
            if h_map.get(s, 0) - 1 < 0:
                return False
            h_map[s] -= 1

        return True


if __name__ == '__main__':
    s = Solution()
    print(s.CheckPermutation(s1="abc", s2="bca"))
    print(s.CheckPermutation(s1="abc", s2="bad"))
