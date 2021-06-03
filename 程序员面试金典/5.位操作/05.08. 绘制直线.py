"""
绘制直线。有个单色屏幕存储在一个一维数组中，使得32个连续像素可以存放在一个 int 里。屏幕宽度为w，且w可被32整除（即一个 int 不会分布在两行上），屏幕高度可由数组长度及屏幕宽度推算得出。请实现一个函数，绘制从点(x1, y)到点(x2, y)的水平线。

给出数组的长度 length，宽度 w（以比特为单位）、直线开始位置 x1（比特为单位）、直线结束位置 x2（比特为单位）、直线所在行数 y。返回绘制过后的数组。

示例1:

 输入：length = 1, w = 32, x1 = 30, x2 = 31, y = 0
 输出：[3]
 说明：在第0行的第30位到第31为画一条直线，屏幕表示为[0b000000000000000000000000000000011]
示例2:

 输入：length = 3, w = 96, x1 = 0, x2 = 95, y = 0
 输出：[-1, -1, -1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/draw-line-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def drawLine(self, length: int, w: int, x1: int, x2: int, y: int) -> List[int]:
        #########对Python3很不友好
        dot = [[0 for _ in range(32)] for _ in range(length)]
        for i in range(x1, x2 + 1):
            idx = (w // 32) * y + (i // 32)
            dot[idx][i % 32] = 1
        # print(dot)

        res = []
        for a in dot:
            int_32bit = 0
            if a[0] == 0:  # 是正数
                for k in range(32):
                    int_32bit += a[k] * 2 ** (31 - k)
            else:  # 是负数
                sign = -1
                # 正数 原码=反码=补码。 负数 补码 = 原码按位取反，末位+1
                # 1.先末位-1
                for k in range(31, -1, -1):
                    if a[k] == 0:
                        a[k] = 1  # 从前面借位，减的
                    else:
                        a[k] = 0  # 借的那个，被借没了
                        break
                # 2.按位取反
                for k in range(1, 32):
                    a[k] = 1 - a[k]
                # 3.计算数值部分
                for k in range(1, 32):
                    int_32bit += a[k] * 2 ** (31 - k)
                # 4.别忘了-
                int_32bit *= (-1)

            res.append(int_32bit)

        return res
