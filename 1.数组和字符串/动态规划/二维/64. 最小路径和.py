"""
给定一个包含非负整数的 mxn网格grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
说明：每次只能向下或者向右移动一步。

示例 1：
输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
输出：7
解释：因为路径 1→3→1→1→1 的总和最小。

示例 2：
输入：grid = [[1,2,3],[4,5,6]]
输出：12

提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-path-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
import math


class Solution:
    # 动态规划，52 ms，80.67%
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                up = dp[i - 1][j] if i - 1 >= 0 else float('inf')
                left = dp[i][j - 1] if j - 1 >= 0 else float('inf')
                dp[i][j] = (0 if math.isinf(up) and math.isinf(left) else min(up, left)) + grid[i][
                    j]
        return dp[-1][-1]


if __name__ == '__main__':
    s = Solution()
    print(s.minPathSum(grid=[[1, 3, 1],
                             [1, 5, 1],
                             [4, 2, 1]]))
    print(s.minPathSum([[1]]))
    print(s.minPathSum(grid=[[1, 2, 3], [4, 5, 6]]))

    import random as r

    print(s.minPathSum([[r.randint(1, 200)] * 200 for _ in range(200)]))
