"""
在给定的二维二进制数组A中，存在两座岛。（岛是由四面相连的 1 形成的一个最大组。）

现在，我们可以将0变为1，以使两座岛连接起来，变成一座岛。

返回必须翻转的0 的最小数目。（可以保证答案至少是 1 。）



示例 1：

输入：A = [[0,1],[1,0]]
输出：1
示例 2：

输入：A = [[0,1,0],[0,0,0],[0,0,1]]
输出：2
示例 3：

输入：A = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
输出：1


提示：

2 <= A.length == A[0].length <= 100
A[i][j] == 0 或 A[i][j] == 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shortest-bridge
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
from typing import List


class Solution:
    """
    先通过DFS将一个岛屿中的1全部改名为2，并且记录下这个岛屿的所有坐标存入point_list中。
由point_list中的点开始，通过BFS一层一层的靠近另一个岛屿，一碰到另一个岛屿（标记为1）,直接返回记录的层数-1即可。

作者：westqi
链接：https://leetcode-cn.com/problems/shortest-bridge/solution/934-zui-duan-de-qiao-by-westqi-zk2a/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def shortestBridge(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def DFS(i, j):
            if i < 0 or i > m - 1 or j < 0 or j > n - 1:
                return
            if grid[i][j] != 1:
                return
            if grid[i][j] == 1:
                grid[i][j] = 2
                point_list.append((i, j))  ## 装入BFS初始要搜索的点
            DFS(i + 1, j)
            DFS(i - 1, j)
            DFS(i, j + 1)
            DFS(i, j - 1)

        def BFS(root_list):
            queue = collections.deque()
            visited = set()
            for ele in root_list:
                queue.append((ele, 0))
                visited.add(ele)
            while queue:
                (ni, nj), nd = queue.popleft()
                if grid[ni][nj] == 1:  # 遇到另一个岛屿
                    return nd - 1
                for i, j in [(ni - 1, nj), (ni + 1, nj), (ni, nj + 1), (ni, nj - 1)]:
                    if i >= 0 and i <= m - 1 and j >= 0 and j <= n - 1:
                        if (i, j) not in visited:
                            visited.add((i, j))
                            queue.append(((i, j), nd + 1))

            return "NO ANSWER"

        ## 先把其中一个岛屿命名为2，并且把这个岛屿所有坐标装入point_list
        flag = 0
        point_list = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    DFS(i, j)
                    flag = 1
                    break
            if flag:  ## 用来跳出两重循环
                break
        return BFS(point_list)


if __name__ == '__main__':
    s = Solution()
