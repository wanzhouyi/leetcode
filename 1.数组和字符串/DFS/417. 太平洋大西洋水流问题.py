"""
给定一个 m x n 的非负整数矩阵来表示一片大陆上各个单元格的高度。
“太平洋”处于大陆的左边界和上边界，而“大西洋”处于大陆的右边界和下边界。
规定水流只能按照上、下、左、右四个方向流动，且只能从高到低或者在同等高度上流动。
请找出那些水流既可以流动到“太平洋”，又能流动到“大西洋”的陆地单元的坐标。

提示：
输出坐标的顺序不重要
m 和 n 都小于150

示例：
给定下面的 5x5 矩阵:

  太平洋 ~   ~   ~   ~   ~ 
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * 大西洋

返回:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (上图中带括号的单元).

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/pacific-atlantic-water-flow
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    # DFS，316ms，71%
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        if matrix and matrix[0]:
            m, n = len(matrix), len(matrix[0])
        else:
            return []

        def dfs(x, y, sea: set):
            if (x, y) not in sea:
                sea.add((x, y))
                for x0, y0 in directions:
                    x1, y1 = x + x0, y + y0
                    if 0 <= x1 <= m - 1 \
                            and 0 <= y1 <= n - 1 \
                            and (x1, y1) not in sea \
                            and matrix[x1][y1] >= matrix[x][y]:
                        dfs(x1, y1, sea)

        for i in range(n):
            dfs(0, i, pacific)
            dfs(m - 1, i, atlantic)

        for j in range(m):
            dfs(j, 0, pacific)
            dfs(j, n - 1, atlantic)
        inter = pacific.intersection(atlantic)
        return [list(tp) for tp in inter]


if __name__ == '__main__':
    s = Solution()
    print(s.pacificAtlantic(
        [[1, 2, 2, 3, 5],
         [3, 2, 3, 4, 4],
         [2, 4, 5, 3, 1],
         [6, 7, 1, 4, 5],
         [5, 1, 1, 2, 4]]))
    # 注意空数组
    print(s.pacificAtlantic([]))
