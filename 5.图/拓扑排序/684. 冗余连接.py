"""
在本问题中, 树指的是一个连通且无环的无向图。
输入一个图，该图由一个有着N个节点 (节点值不重复1, 2, ..., N) 的树及一条附加的边构成。
附加的边的两个顶点包含在1到N中间，这条附加的边不属于树中已存在的边。
结果图是一个以边组成的二维数组。每一个边的元素是一对[u, v]，满足u < v，表示连接顶点u和v的无向图的边。
返回一条可以删去的边，使得结果图是一个有着N个节点的树。如果有多个答案，则返回二维数组中最后出现的边。
答案边[u, v] 应满足相同的格式u < v。

示例 1：

输入: [[1,2], [1,3], [2,3]]
输出: [2,3]
解释: 给定的无向图为:
  1
 / \
2 - 3

示例 2：

输入: [[1,2], [2,3], [3,4], [1,4], [1,5]]
输出: [1,4]
解释: 给定的无向图为:
5 - 1 - 2
    |   |
    4 - 3
注意:

输入的二维数组大小在 3 到 1000。
二维数组中的整数在1到N之间，其中N是输入数组的大小。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/redundant-connection
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    # 方法一，拓扑排序，60ms，89%
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        from collections import defaultdict
        veges = defaultdict(list)
        for edge in edges:
            p1, p2 = edge[0], edge[1]
            veges[p1].append(p2)
            veges[p2].append(p1)
        # print(veges)
        vege1 = [point for point in veges.keys() if len(veges[point]) == 1]
        while vege1:
            p = vege1.pop()
            q = veges[p][0]
            veges.pop(p)
            veges[q].remove(p)
            if len(veges[q]) == 1:
                vege1.append(q)
        for edge in edges[::-1]:
            p1, p2 = edge[0], edge[1]
            if p2 in veges[p1]:
                return edge

        # 官解并查集
        def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
            """
            在一棵树中，边的数量比节点的数量少 1。如果一棵树有 N 个节点，则这棵树有 N-1条边。
            这道题中的图在树的基础上多了一条附加的边，因此边的数量也是 N。
            树是一个连通且无环的无向图，在树中多了一条附加的边之后就会出现环，因此附加的边即为导致环出现的边。
            可以通过并查集寻找附加的边。初始时，每个节点都属于不同的连通分量。
            遍历每一条边，判断这条边连接的两个顶点是否属于相同的连通分量。
            如果两个顶点属于不同的连通分量，则说明在遍历到当前的边之前，这两个顶点之间不连通，
            因此当前的边不会导致环出现，合并这两个顶点的连通分量。
            如果两个顶点属于相同的连通分量，则说明在遍历到当前的边之前，这两个顶点之间已经连通，
            因此当前的边导致环出现，为附加的边，将当前的边作为答案返回。
            """
            nodesCount = len(edges)
            parent = list(range(nodesCount + 1))

            def find(index: int) -> int:
                if parent[index] != index:
                    parent[index] = find(parent[index])
                return parent[index]

            def union(index1: int, index2: int):
                parent[find(index1)] = find(index2)

            for node1, node2 in edges:
                if find(node1) != find(node2):
                    union(node1, node2)
                else:
                    return [node1, node2]

            return []


if __name__ == '__main__':
    s = Solution()
    print(s.findRedundantConnection([[1, 2], [1, 3], [2, 3]]))
    print(s.findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]))
