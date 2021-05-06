"""
编写一种算法，若M × N矩阵中某个元素为0，则将其所在的行与列清零。


示例 1：

输入：
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
输出：
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
示例 2：

输入：
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
输出：
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zero-matrix-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        方法一，暴力法,64ms
        """
        m, n = len(matrix), len(matrix[0])
        if m == 0 or n == 0: return
        rows, columns = set(), set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    columns.add(j)

        zero_row = [0] * n
        for r in rows:
            matrix[r] = zero_row

        for c in columns:
            for idx in range(m):
                matrix[idx][c] = 0

        print(matrix)

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        官解：方法一：使用标记数组
        我们可以用两个标记数组分别记录每一行和每一列是否有零出现。
        具体地，我们首先遍历该数组一次，如果某个元素为 0，那么就将该元素所在的行和列所对应标记数组的位置置为true。
        最后我们再次遍历该数组，用标记数组更新原数组即可。
        """
        m, n = len(matrix), len(matrix[0])
        row, col = [False] * m, [False] * n

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row[i] = col[j] = True

        for i in range(m):
            for j in range(n):
                if row[i] or col[j]:
                    matrix[i][j] = 0


if __name__ == '__main__':
    s = Solution()
    # print(s.setZeroes([[1,1,1],[1,0,1],[1,1,1]]))
    print(s.setZeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]))
