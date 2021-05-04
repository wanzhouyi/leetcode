"""
字符串有三种编辑操作:插入一个字符、删除一个字符或者替换一个字符。
给定两个字符串，编写一个函数判定它们是否只需要一次(或者零次)编辑。

示例1:
输入:
first = "pale"
second = "ple"
输出: True
示例2:
输入:
first = "pales"
second = "pal"
输出: False

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/one-away-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        n1, n2 = len(first), len(second)
        if abs(n1 - n2) > 1:
            return False
        elif n1 == 0 or n2 == 0:
            return True
        if n1 == n2:
            for i in range(n1):
                if first[i] != second[i]:
                    if first[i + 1:] != second[i + 1:]:
                        return False
                    break
        elif n1 > n2:
            for i in range(n1):
                if i < n2 and first[i] != second[i]:
                    if first[i + 1:] != second[i:]:
                        return False
                    break
        elif n2 > n1:
            for j in range(n2):
                if j < n1 and second[j] != first[j]:
                    if second[j + 1:] != first[j:]:
                        return False
                    break
        return True


if __name__ == '__main__':
    s = Solution()
    # print(s.oneEditAway(first="pale", second="ple"))
    # print(s.oneEditAway(first="pales", second="pal"))
    # print(s.oneEditAway('a', 'a'))
    # print(s.oneEditAway('', ''))
    # print(s.oneEditAway(first="pal", second="pales"))
    # print(s.oneEditAway('', 'a'))
    print(s.oneEditAway('a', 'ab'))
