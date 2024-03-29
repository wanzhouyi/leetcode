"""
给定一个赎金信 (ransom) 字符串和一个杂志(magazine)字符串，
判断第一个字符串 ransom 能不能由第二个字符串 magazines 里面的字符构成。
如果可以构成，返回 true ；否则返回 false。

(题目说明：为了不暴露赎金信字迹，要从杂志上搜索各个需要的字母，组成单词来表达意思。
杂志字符串中的每个字符只能在赎金信字符串中使用一次。)

注意：
你可以假设两个字符串均只含有小写字母。

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ransom-note
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    # 方法一，使用Counter，52ms
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        ct_ransom = Counter(ransomNote)
        ct_magazine = Counter(magazine)
        return all(map(lambda x: ct_ransom[x] <= ct_magazine[x], ct_ransom.keys()))



if __name__ == '__main__':
    s = Solution()
    print(s.canConstruct("a", "b"))
    print(s.canConstruct("aa", "ab"))
    print(s.canConstruct("aa", "aab"))
