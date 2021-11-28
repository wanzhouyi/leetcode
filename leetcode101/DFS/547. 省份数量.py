"""
有 n 个城市，其中一些彼此相连，另一些没有相连。
如果城市 a 与城市 b 直接相连，且城市 b 与城市 c 直接相连，那么城市 a 与城市 c 间接相连。

省份 是一组直接或间接相连的城市，组内不含其他没有相连的城市。

给你一个 n x n 的矩阵 isConnected ，其中 isConnected[i][j] = 1 表示第 i 个城市和第 j 个城市直接相连，
而 isConnected[i][j] = 0 表示二者不直接相连。

返回矩阵中 省份 的数量。

示例 1：


输入：isConnected = [[1,1,0],[1,1,0],[0,0,1]]
输出：2
示例 2：


输入：isConnected = [[1,0,0],[0,1,0],[0,0,1]]
输出：3


提示：

1 <= n <= 200
n == isConnected.length
n == isConnected[i].length
isConnected[i][j] 为 1 或 0
isConnected[i][i] == 1
isConnected[i][j] == isConnected[j][i]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-provinces
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        m = len(isConnected)
        ans = 0
        visited = set()

        def dfs(x):
            visited.add(x)
            for y in range(m):
                if isConnected[x][y] == 1 and y not in visited:
                    dfs(y)

        for i in range(m):
            if i not in visited:
                ans += 1
                dfs(i)
        return ans


# 以下是官解
class Solution:
    """
    方法一：深度优先搜索
    深度优先搜索的思路是很直观的。遍历所有城市，对于每个城市，如果该城市尚未被访问过，则从该城市开始深度优先搜索，
    通过矩阵 isConnected 得到与该城市直接相连的城市有哪些，这些城市和该城市属于同一个连通分量，
    然后对这些城市继续深度优先搜索，直到同一个连通分量的所有城市都被访问到，即可得到一个省份。
    遍历完全部城市以后，即可得到连通分量的总数，即省份的总数。

    作者：LeetCode-Solution
    链接：https://leetcode-cn.com/problems/number-of-provinces/solution/sheng-fen-shu-liang-by-leetcode-solution-eyk0/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(i: int):
            for j in range(provinces):
                if isConnected[i][j] == 1 and j not in visited:
                    visited.add(j)
                    dfs(j)

        provinces = len(isConnected)
        visited = set()
        circles = 0

        for i in range(provinces):
            if i not in visited:
                dfs(i)
                circles += 1

        return circles


class Solution:
    """
    方法二：广度优先搜索
    也可以通过广度优先搜索的方法得到省份的总数。对于每个城市，如果该城市尚未被访问过，则从该城市开始广度优先搜索，
    直到同一个连通分量中的所有城市都被访问到，即可得到一个省份。
    """

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = len(isConnected)
        visited = set()
        circles = 0

        for i in range(provinces):
            if i not in visited:
                Q = collections.deque([i])
                while Q:
                    j = Q.popleft()
                    visited.add(j)
                    for k in range(provinces):
                        if isConnected[j][k] == 1 and k not in visited:
                            Q.append(k)
                circles += 1

        return circles


class Solution:
    """方法三：并查集
计算连通分量数的另一个方法是使用并查集。初始时，每个城市都属于不同的连通分量。遍历矩阵 \textit{isConnected}isConnected，如果两个城市之间有相连关系，则它们属于同一个连通分量，对它们进行合并。

遍历矩阵 \textit{isConnected}isConnected 的全部元素之后，计算连通分量的总数，即为省份的总数。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/number-of-provinces/solution/sheng-fen-shu-liang-by-leetcode-solution-eyk0/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。"""

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def find(index: int) -> int:
            if parent[index] != index:
                parent[index] = find(parent[index])
            return parent[index]

        def union(index1: int, index2: int):
            parent[find(index1)] = find(index2)

        provinces = len(isConnected)
        parent = list(range(provinces))

        for i in range(provinces):
            for j in range(i + 1, provinces):
                if isConnected[i][j] == 1:
                    union(i, j)

        circles = sum(parent[i] == i for i in range(provinces))
        return circles


if __name__ == '__main__':
    s = Solution()
    print(s.findCircleNum(isConnected=[[1, 1, 0],
                                       [1, 1, 0],
                                       [0, 0, 1]]))
