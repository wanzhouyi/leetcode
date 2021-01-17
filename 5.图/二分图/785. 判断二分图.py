"""
给定一个无向图graph，当这个图为二分图时返回true。
如果我们能将一个图的节点集合分割成两个独立的子集A和B，并使图中的每一条边的两个节点一个来自A集合，一个来自B集合，
我们就将这个图称为二分图。
graph将会以邻接表方式给出，graph[i]表示图中与节点i相连的所有节点。
每个节点都是一个在0到graph.length-1之间的整数。这图中没有自环和平行边：graph[i]中不存在i，并且graph[i]中没有重复的值。

示例 1:
输入: [[1,3], [0,2], [1,3], [0,2]]
输出: true
解释: 
无向图如下:
0----1
|    |
|    |
3----2
我们可以将节点分成两组: {0, 2} 和 {1, 3}。

示例 2:
输入: [[1,2,3], [0,2], [0,1,3], [0,2]]
输出: false
解释: 
无向图如下:
0----1
| \  |
|  \ |
3----2
我们不能将节点分割成两个独立的子集。
注意:

graph 的长度范围为 [1, 100]。
graph[i] 中的元素的范围为 [0, graph.length - 1]。
graph[i] 不会包含 i 或者有重复的值。
图是无向的: 如果j 在 graph[i]里边, 那么 i 也会在 graph[j]里边。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/is-graph-bipartite
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    # 方法一，队列+BFS，68ms，39.15%
    def isBipartite(self, graph: List[List[int]]) -> bool:
        from collections import deque, defaultdict
        # 图的顶点个数
        n = len(graph)
        # 如果图的顶点个数为0，直接返回False
        if n == 0:
            return False
        # 颜色记录，0表示未染色，1和2表示染成的两种颜色
        color = defaultdict(int)
        dq = deque()
        for i in range(n):
            # 未被染色的点
            if color[i] == 0:
                # 将当前点的颜色设为1
                color[i] = 1
                # 将当前点加入BFS队列
                dq.append(i)

            while dq:
                node_father = dq.popleft()
                for node_son in graph[node_father]:
                    if color[node_son] == 0:
                        dq.append(node_son)
                        color[node_son] = (1 if color[node_father] == 2 else 2)
                    elif color[node_father] == color[node_son]:
                        return False
        return True

    # 方法二，官解BFS，
    def isBipartite(self, graph: List[List[int]]) -> bool:
        import collections
        n = len(graph)
        UNCOLORED, RED, GREEN = 0, 1, 2
        color = [UNCOLORED] * n

        for i in range(n):
            if color[i] == UNCOLORED:
                q = collections.deque([i])
                color[i] = RED
                while q:
                    node = q.popleft()
                    cNei = (GREEN if color[node] == RED else RED)
                    for neighbor in graph[node]:
                        if color[neighbor] == UNCOLORED:
                            q.append(neighbor)
                            color[neighbor] = cNei
                        elif color[neighbor] != cNei:
                            return False

        return True

    # 方法三，官解DFS
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        UNCOLORED, RED, GREEN = 0, 1, 2
        color = [UNCOLORED] * n
        valid = True

        def dfs(node: int, c: int):
            nonlocal valid
            color[node] = c
            cNei = (GREEN if c == RED else RED)
            for neighbor in graph[node]:
                if color[neighbor] == UNCOLORED:
                    dfs(neighbor, cNei)
                    if not valid:
                        return
                elif color[neighbor] != cNei:
                    valid = False
                    return

        for i in range(n):
            if color[i] == UNCOLORED:
                dfs(i, RED)
                if not valid:
                    break

        return valid


if __name__ == '__main__':
    s = Solution()
    print(s.isBipartite([[1, 3], [0, 2], [1, 3], [0, 2]]))
    # print(s.isBipartite([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]))
    # print(s.isBipartite([[1], [0, 3], [3], [1, 2]]))
    # print(s.isBipartite([[3], [2, 4], [1], [0, 4], [1, 3]]))
