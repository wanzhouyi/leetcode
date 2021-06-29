"""
给定一个正整数，返回它在 Excel 表中相对应的列名称。

例如，
    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...
示例 1:

输入: 1
输出: "A"
示例2:

输入: 28
输出: "AB"
示例3:

输入: 701
输出: "ZY"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/excel-sheet-column-title
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = list()
        while columnNumber > 0:
            a0 = (columnNumber - 1) % 26 + 1
            ans.append(chr(a0 - 1 + ord("A")))
            columnNumber = (columnNumber - a0) // 26
        return "".join(ans[::-1])


class Solution:
    """
    思路和心得：

    1.26进制无疑

    2.但是从1开始

    每次计算都要 -1
    """

    def convertToTitle(self, columnNumber: int) -> str:
        n = columnNumber

        res = ""
        while n:
            n -= 1
            tmp = n % 26
            res = chr(ord('A') + tmp) + res
            n //= 26
        return res
