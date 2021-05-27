"""
整数转换。编写一个函数，确定需要改变几个位才能将整数A转成整数B。

示例1:

 输入：A = 29 （或者0b11101）, B = 15（或者0b01111）
 输出：2
示例2:

 输入：A = 1，B = 2
 输出：2
提示:

A，B范围在[-2147483648, 2147483647]之间

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/convert-integer-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def convertInteger(self, A: int, B: int) -> int:
        return bin((A & 0xffffffff) ^ (B & 0xffffffff)).count('1')


if __name__ == '__main__':
    s = Solution()
    print(s.convertInteger(29, 15))
    print(s.convertInteger(1, 2))
    print(s.convertInteger(2147483647, -2147483647))
    print(s.convertInteger(826966453, -729934991))
