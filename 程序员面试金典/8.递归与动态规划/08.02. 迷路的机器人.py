"""
设想有个机器人坐在一个网格的左上角，网格 r 行 c 列。机器人只能向下或向右移动，但不能走到一些被禁止的网格（有障碍物）。设计一种算法，寻找机器人从左上角移动到右下角的路径。



网格中的障碍物和空位置分别用 1 和 0 来表示。

返回一条可行的路径，路径由经过的网格的行号和列号组成。左上角为 0 行 0 列。如果没有可行的路径，返回空数组。

示例1:

输入:
[
 [0,0,0],
 [0,1,0],
 [0,0,0]
]
输出: [[0,0],[0,1],[0,2],[1,2],[2,2]]
解释: 
输入中标粗的位置即为输出表示的路径，即
0行0列（左上角） -> 0行1列 -> 0行2列 -> 1行2列 -> 2行2列（右下角）
说明：r和 c 的值均不超过 100。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/robot-in-a-grid-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    """
    回溯法
    """

    def pathWithObstacles(self, obstacleGrid: List[List[int]]) -> List[List[int]]:
        if not obstacleGrid or not obstacleGrid[0]:
            return []
        r, c = len(obstacleGrid), len(obstacleGrid[0])
        directs = [(0, 1), (1, 0)]
        visited = set()
        way = []

        def back_track(pnt, path):
            nonlocal way
            if way:
                return
            if obstacleGrid[pnt[0]][pnt[1]] == 1:
                return
            if pnt == (r - 1, c - 1) and obstacleGrid[r - 1][c - 1] == 0:
                path.insert(0, (0, 0))
                way = path.copy()
            visited.add(pnt)

            for x1, y1 in directs:
                new_pnt_x, new_pnt_y = pnt[0] + x1, pnt[1] + y1
                if 0 <= new_pnt_x < r \
                        and 0 <= new_pnt_y < c \
                        and (new_pnt_x, new_pnt_y) not in visited \
                        and obstacleGrid[new_pnt_x][new_pnt_y] != 1:
                    path.append((new_pnt_x, new_pnt_y))
                    back_track((new_pnt_x, new_pnt_y), path)
                    path.pop()

        back_track((0, 0), [])
        return list(map(lambda x: list(x), way))


class Solution:
    """
    网格中中的动态规划算法，其状态转移方程可以归纳为如下：

    最短路径（带权值的网格）：dp[i][j] = min{dp[i - 1][j], dp[i][j - 1]} + grid[i][j]
    所有路径（包含障碍，1表示障碍，0表示通行）：if grid[i][j] ==0 :dp[i][j] = dp[i - 1][j] + dp[i][j - 1],否则,dp[i][j] = 0
    所有路径（不包含障碍）,状态方程同2中if，也可以直接返回组合数C(m+n)(m)，m，n为网格的行数和列数。
    本题：一条路径，状态方程和1一样，只不过每个点的权值相等。
    思路：我们可以通过状态方程1去递归求解一条路径（m + n），并且当grid[i][j] = 1时，令dp[i][j] = m + n + 1。最后我们只需要判断dp[m - 1][n - 1]是否等于m+n就可以知道是否存在一条路径，由于本题不仅仅需要考虑是否存在一条路径，还需要返回所经过的每一个点，因此我们需要一个记录每次状态转移来源的矩阵pos。在计算状态转移方程时，同时记录当前pos[i][j]为来源的点。最后我们从右下角进行溯源，从而找到所有路径上的所有点。

    作者：lzx1997
    链接：https://leetcode-cn.com/problems/robot-in-a-grid-lcci/solution/tong-yi-de-dpmo-ban-qiu-jie-ju-zhen-zhon-w3pg/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def __init__(self):
        self.path = []

    def pathWithObstacles(self, obstacleGrid: List[List[int]]) -> List[List[int]]:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] or obstacleGrid[m - 1][n - 1]:
            return []
        # 1. 定义状态矩阵，记录每一个状态最优解，自底向上求解最优解
        dp = [[m + n + 1] * n for _ in range(m)]  # 记录从起点到[i][j]的步数
        pos = [[-1] * n for _ in range(m)]  # 记录状态来源，比如，用1表示往下，2表示往右

        # 2. 边界初始化
        pos[0][0] = 0
        dp[0][0] = 0
        for i in range(1, m):
            if obstacleGrid[i][0] != 1:
                dp[i][0] = i
                pos[i][0] = 1
            else:
                break
        for j in range(1, n):
            if obstacleGrid[0][j] != 1:
                dp[0][j] = j
                pos[0][j] = 2
            else:
                break
        # 通过状态转移方程计算所有状态的最优解，同时，根据题目需要记录状态转移来源
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0 and (
                        dp[i - 1][j] != m + n + 1 or dp[i][j - 1] != m + n + 1):
                    if dp[i - 1][j] < dp[i][j - 1]:
                        dp[i][j] = dp[i - 1][j] + 1
                        pos[i][j] = 1  # 来自上边
                    else:
                        dp[i][j] = dp[i][j - 1] + 1
                        pos[i][j] = 2  # 来自左边
        if dp[m - 1][n - 1] == m + n + 1:  # 判断是否存在路径
            return []
        else:
            x, y = m - 1, n - 1
            res = [[x, y]]
            while pos[x][y] != 0:  # 溯源，直到起点
                t = pos[x][y]
                if t == 1:
                    x -= 1
                else:
                    y -= 1
                res.append([x, y])
            res.reverse()  # 反转，形成一条从起点到终点的路径。

            return res


if __name__ == '__main__':
    s = Solution()
    # print(s.pathWithObstacles([
    #     [0, 0, 0],
    #     [0, 1, 0],
    #     [0, 0, 0]
    # ]))
    # print(s.pathWithObstacles([
    #     [0, 1, 0],
    #     [1, 1, 0],
    #     [0, 0, 0]
    # ]))
    # print(s.pathWithObstacles([]))
    # print(s.pathWithObstacles([[]]))
    print(s.pathWithObstacles([[1]]))
    print(s.pathWithObstacles([[0]]))
