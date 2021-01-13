"""
给定一个 n×n 的二维矩阵表示一个图像。
将图像顺时针旋转 90 度。
说明：
你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。
示例 1:
给定 matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],
原地旋转输入矩阵，使其变为:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
示例 2:
给定 matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

原地旋转输入矩阵，使其变为:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rotate-image
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    # 方法一，两次旋转，44ms，29%
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        def rotate_up_down():
            up, down = 0, len(matrix) - 1
            while up < down:
                matrix[up], matrix[down] = matrix[down], matrix[up]
                up += 1
                down -= 1

        def rotate_corner():
            for i in range(n):
                for j in range(i, n):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        rotate_up_down()
        rotate_corner()


if __name__ == '__main__':
    s = Solution()
    print(s.rotate(matrix=
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]))
