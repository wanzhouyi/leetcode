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
        """
        方法一：遍历整个数组，选择一个索引进行切片和重新连接，判断是否正确结果
        """
        n1, n2 = len(s1), len(s2)
        if n1 != n2: return False
        if s1 == s2 == "":
            return True
        for i in range(n1):
            if s1[i:] + s1[:i] == s2:
                return True
        return False

    def isFlipedString(self, s1: str, s2: str) -> bool:
        """
        如果首尾一定相连，那么如果把S2的尾巴连上S2的头，那中间应该就是S1
        """
        if len(s1) != len(s2):
            return False
        new = s2 + s2
        return s1 in new

    def isFlipedString(self, s1: str, s2: str) -> bool:
        l1 = len(s1)

        if l1 != len(s2):
            return False

        # 将s1 + s1 叠加起来， 判断子串。
        s1s1 = s1 + s1
        if s1s1.find(s2) != -1:
            return True

        return False
if __name__ == '__main__':
    s = Solution()
    print(s.isFlipedString(s1="waterbottle", s2="erbottlewat"))
    print(s.isFlipedString(s1="aa", s2="aba"))
    print(s.isFlipedString("", ""))
    print(s.isFlipedString("a", "a"))
    print(s.isFlipedString("ab", "ab"))
