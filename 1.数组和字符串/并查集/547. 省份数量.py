"""
有 n 个城市，其中一些彼此相连，另一些没有相连。如果城市 a 与城市 b 直接相连，且城市 b 与城市 c 直接相连，那么城市 a 与城市 c 间接相连。
省份 是一组直接或间接相连的城市，组内不含其他没有相连的城市。
给你一个 n x n 的矩阵 isConnected ，其中 isConnected[i][j] = 1 表示第 i 个城市和第 j 个城市直接相连，而 isConnected[i][j] = 0 表示二者不直接相连。
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
from typing import List


class Solution:
    # 方法一，暴力DFS，44 ms，97.74%
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        group = 0

        def dfs(i):
            if i in visited:
                return
            visited.add(i)
            for j in range(n):
                if isConnected[i][j] == 1:
                    dfs(j)

        for i in range(n):
            if i not in visited:
                group += 1
                dfs(i)
        return group

    # 方法二，暴力BFS，180 ms，9.78%%
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        import collections
        n = len(isConnected)
        visited = set()
        group = 0

        for i in range(n):
            if i not in visited:
                q = collections.deque([i])
                while q:
                    j = q.popleft()
                    visited.add(j)
                    for k in range(n):
                        if isConnected[j][k] == 1 and k not in visited:
                            q.append(k)
                group += 1
        return group

    # 方法三，并查集
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

    # 方法四，并查集（平衡）
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        ls = list(range(n))
        rank = [1] * n

        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i == root_j:
                return
            if rank[root_i] < rank[root_j]:
                root_i, root_j = root_j, root_i
            ls[root_j] = root_i
            rank[root_i] += rank[root_j]

        def find(x):
            if ls[x] == x:
                return x
            else:
                ls[x] = find(ls[x])
                return ls[x]

        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    union(i, j)
        for i in range(n):
            ls[i] = find(i)

        return len(set(ls))


if __name__ == '__main__':
    s = Solution()
    print(s.findCircleNum([[1, 1, 0],
                           [1, 1, 0],
                           [0, 0, 1]]))
    print(s.findCircleNum([[1, 0, 0],
                           [0, 1, 0],
                           [0, 0, 1]]))
