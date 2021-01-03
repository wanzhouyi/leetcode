"""
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

示例1:
输入: s = "anagram", t = "nagaram"
输出: true

示例 2:
输入: s = "rat", t = "car"
输出: false

说明:
你可以假设字符串只包含小写字母。

进阶:
如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-anagram
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    # 方法一，使用Counter，60ms
    def isAnagram(self, s: str, t: str) -> bool:
        #为了保持每个方法的独立性，在方法内import。生产中注意代码规范
        from collections import Counter
        ct_s = Counter(s)
        ct_t = Counter(t)
        if len(ct_t) != len(ct_s):
            return False
        return all(map(lambda key: ct_t[key] == ct_s[key], ct_t.keys()))
    # 方法二，排序后使用指针，68ms
    def isAnagram(self, s: str, t: str) -> bool:
        ls_s=sorted(s)
        ls_t=sorted(t)
        if len(ls_s)!=len(ls_t):
            return False
        for i in range(len(ls_s)):
            if ls_s[i]!=ls_t[i]:
                return False
        return True
    



if __name__ == '__main__':
    s = Solution()
    print(s.isAnagram(s="anagram", t="nagaram"))
    print(s.isAnagram(s="rat", t="car"))
    # 空字符串
    print(s.isAnagram(s="",t=""))
    # 长度不一致的情况
    print(s.isAnagram(s="tsst",t="stt"))
