"""
给定一个二维矩阵，计算其子矩形范围内元素的总和，该子矩阵的左上角为 (row1,col1) ，右下角为 (row2,col2) 。
上图子矩阵左上角(row1, col1) = (2, 1)，右下角(row2, col2) = (4, 3)，该子矩形内元素的总和为 8。
示例：
给定 matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]
sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12
提示：
你可以假设矩阵不可变。
会多次调用sumRegion方法。
你可以假设row1 ≤ row2 且col1 ≤ col2 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/range-sum-query-2d-immutable
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class NumMatrix:
    """
    这里是用一维数组的前缀和模拟二维数组的前缀和
    """

    def __init__(self, matrix: List[List[int]]):
        self.pre_sum = None
        if not matrix or not matrix[0]:
            return
        m, n = len(matrix), len(matrix[0])
        self.pre_sum = [[0] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                self.pre_sum[i].append(self.pre_sum[i][-1] + matrix[i][j])

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if self.pre_sum is None:
            return 0
        ans = 0
        for i in range(row1, row2 + 1):
            ans += self.pre_sum[i][col2 + 1] - self.pre_sum[i][col1]
        return ans


class NumMatrix:
    """
    官解，二维矩阵的前缀和，
    也可参考https://leetcode-cn.com/problems/range-sum-query-2d-immutable/solution/ru-he-qiu-er-wei-de-qian-zhui-he-yi-ji-y-6c21/
    """

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), (len(matrix[0]) if matrix else 0)
        self.sums = [[0] * (n + 1) for _ in range(m + 1)]
        _sums = self.sums

        for i in range(m):
            for j in range(n):
                _sums[i + 1][j + 1] = _sums[i][j + 1] + _sums[i + 1][j] - _sums[i][j] + matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        _sums = self.sums

        return _sums[row2 + 1][col2 + 1] - _sums[row1][col2 + 1] - _sums[row2 + 1][col1] + \
               _sums[row1][col1]
