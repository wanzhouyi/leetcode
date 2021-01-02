"""
给定一个正整数n，生成一个包含 1 到n平方所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。

示例:
输入: 3
输出:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/spiral-matrix-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    # 方法一，暴力法，44ms
    def generateMatrix(self, n: int) -> List[List[int]]:
        x, y = 0, 0
        matrix = [[0] * n for _ in range(n)]
        current_direct = 'E'
        counter = 0
        while counter < n ** 2:
            counter += 1
            matrix[x][y] = counter
            if current_direct == 'E':
                if y + 1 == n or matrix[x][y + 1] != 0:
                    current_direct = 'S'
                    x += 1
                else:
                    y += 1
            elif current_direct == 'S':
                if x + 1 == n or matrix[x + 1][y] != 0:
                    current_direct = 'W'
                    y -= 1
                else:
                    x += 1
            elif current_direct == 'W':
                if y - 1 < 0 or matrix[x][y - 1] != 0:
                    current_direct = 'N'
                    x -= 1
                else:
                    y -= 1
            elif current_direct == 'N':
                if x - 1 < 0 or matrix[x - 1][y] != 0:
                    current_direct = 'E'
                    y += 1
                else:
                    x -= 1
        return matrix


if __name__ == '__main__':
    s = Solution()
    print(s.generateMatrix(1))
    print(s.generateMatrix(2))
    print(s.generateMatrix(3))
    print(s.generateMatrix(4))
    print(s.generateMatrix(5))
