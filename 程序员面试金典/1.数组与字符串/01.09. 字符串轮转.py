"""
字符串轮转。给定两个字符串s1和s2，请编写代码检查s2是否为s1旋转而成（比如，waterbottle是erbottlewat旋转后的字符串）。
示例1:

 输入：s1 = "waterbottle", s2 = "erbottlewat"
 输出：True
示例2:

 输入：s1 = "aa", s2 = "aba"
 输出：False
提示：

字符串长度在[0, 100000]范围内。
说明:

你能只调用一次检查子串的方法吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/string-rotation-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 != n2: return False
        if s1 == s2 == "":
            return True
        for i in range(n1):
            if s1[i:] + s1[:i] == s2:
                return True
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.isFlipedString(s1="waterbottle", s2="erbottlewat"))
    print(s.isFlipedString(s1="aa", s2="aba"))
    print(s.isFlipedString("", ""))
    print(s.isFlipedString("a", "a"))
    print(s.isFlipedString("ab", "ab"))
