"""
给定一个由 0 和 1 组成的矩阵，找出每个元素到最近的 0 的距离。
两个相邻元素间的距离为 1 。

示例 1：
输入：
[[0,0,0],
 [0,1,0],
 [0,0,0]]
输出：
[[0,0,0],
[0,1,0],
[0,0,0]]

示例 2：
输入：
[[0,0,0],
 [0,1,0],
 [1,1,1]]
输出：
[[0,0,0],
 [0,1,0],
 [1,2,1]]


提示：

给定矩阵的元素个数不超过 10000。
给定矩阵中至少有一个元素是 0。
矩阵中的元素只在四个方向上相邻: 上、下、左、右。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/01-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
from math import isnan


class Solution:
    # 方法一，BFS，728 ms，61.42%
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        dp = [[None] * n for _ in range(m)]
        stack = set([(x, y) for x in range(m) for y in range(n) if matrix[x][y] == 0])
        counter = 0
        while stack:
            temp_stack = stack.copy()
            stack.clear()
            for x, y in temp_stack:
                dp[x][y] = counter
                for i, j in directions:
                    new_x, new_y = x + i, y + j
                    if 0 <= new_x <= m - 1 \
                            and 0 <= new_y <= n - 1 \
                            and (new_x, new_y) not in temp_stack \
                            and dp[new_x][new_y] is None:
                        stack.add((new_x, new_y))
            counter += 1
        return dp

    # 方法二，官解，动态规划
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        # 初始化动态规划的数组，所有的距离值都设置为一个很大的数
        dist = [[10 ** 9] * n for _ in range(m)]
        # 如果 (i, j) 的元素为 0，那么距离为 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    dist[i][j] = 0
        # 只有 水平向左移动 和 竖直向上移动，注意动态规划的计算顺序
        for i in range(m):
            for j in range(n):
                if i - 1 >= 0:
                    dist[i][j] = min(dist[i][j], dist[i - 1][j] + 1)
                if j - 1 >= 0:
                    dist[i][j] = min(dist[i][j], dist[i][j - 1] + 1)
        # 只有 水平向左移动 和 竖直向下移动，注意动态规划的计算顺序
        for i in range(m - 1, -1, -1):
            for j in range(n):
                if i + 1 < m:
                    dist[i][j] = min(dist[i][j], dist[i + 1][j] + 1)
                if j - 1 >= 0:
                    dist[i][j] = min(dist[i][j], dist[i][j - 1] + 1)
        # 只有 水平向右移动 和 竖直向上移动，注意动态规划的计算顺序
        for i in range(m):
            for j in range(n - 1, -1, -1):
                if i - 1 >= 0:
                    dist[i][j] = min(dist[i][j], dist[i - 1][j] + 1)
                if j + 1 < n:
                    dist[i][j] = min(dist[i][j], dist[i][j + 1] + 1)
        # 只有 水平向右移动 和 竖直向下移动，注意动态规划的计算顺序
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i + 1 < m:
                    dist[i][j] = min(dist[i][j], dist[i + 1][j] + 1)
                if j + 1 < n:
                    dist[i][j] = min(dist[i][j], dist[i][j + 1] + 1)
        return dist


if __name__ == '__main__':
    s = Solution()
    print(s.updateMatrix([[0, 0, 0],
                          [0, 1, 0],
                          [0, 0, 0]]))
    print(s.updateMatrix([[0, 0, 0],
                          [0, 1, 0],
                          [1, 1, 1]]))
    print(s.updateMatrix([[0]]))
