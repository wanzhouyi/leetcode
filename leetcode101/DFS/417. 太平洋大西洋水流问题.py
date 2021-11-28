"""
417. 太平洋大西洋水流问题
给定一个 m x n 的非负整数矩阵来表示一片大陆上各个单元格的高度。“太平洋”处于大陆的左边界和上边界，
而“大西洋”处于大陆的右边界和下边界。
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
"""
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        s1, s2 = set(), set()
        ways = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m, n = len(heights), len(heights[0])

        def dfs(x, y, st: set):
            if (x, y) in st:
                return
            else:
                st.add((x, y))
            for x1, y1 in ways:
                xn = x + x1
                yn = y + y1
                if 0 <= xn <= m - 1 and 0 <= yn <= n - 1 and heights[xn][yn] >= heights[x][y]:
                    dfs(xn, yn, st)

        for i in range(m):
            dfs(i, 0, s1)
            dfs(i, n - 1, s2)
        for j in range(n):
            dfs(0, j, s1)
            dfs(m - 1, j, s2)
        return list(s1.intersection(s2))


if __name__ == '__main__':
    s = Solution()
    print(s.pacificAtlantic())
