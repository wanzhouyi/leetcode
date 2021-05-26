"""
二进制数转字符串。给定一个介于0和1之间的实数（如0.72），类型为double，打印它的二进制表达式。如果该数字无法精确地用32位以内的二进制表示，则打印“ERROR”。

示例1:

 输入：0.625
 输出："0.101"
示例2:

 输入：0.1
 输出："ERROR"
 提示：0.1无法被二进制准确表示
提示：

32位包括输出中的"0."这两位。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/bianry-number-to-string-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def printBin(self, num: float) -> str:
        """
        乘二取整法
        思路
        本题考察的知识点是十进制小数转二进制小数，应用常规方法乘二取整即可求解
        算法
        res初始化为"0."
        在满足位数要求的情况下，当num大于0时，循环
        先将num乘以2，将乘积赋值给num
        取num的个位（0或1），将对应的字符加入res的末尾
        截取num的小数部分，作为num的新值
        最后判断，当num为0时（即res已经精确地表达了num），返回res
        否则，返回"ERROR"

        """
        ct = 30
        res = '0.'
        while num > 0 and ct > 0:
            num *= 2
            if num >= 1:
                res += '1'
                num -= 1
            else:
                res += '0'
            ct -= 1
        return res if not num else 'ERROR'


if __name__ == '__main__':
    s = Solution()
    print(s.printBin(0.625))
    print(s.printBin(0.1))
