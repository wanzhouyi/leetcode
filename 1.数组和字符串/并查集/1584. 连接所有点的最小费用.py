"""
给你一个points数组，表示 2D 平面上的一些点，其中points[i] = [xi, yi]。
连接点[xi, yi] 和点[xj, yj]的费用为它们之间的 曼哈顿距离：|xi - xj| + |yi - yj|，其中|val|表示val的绝对值。
请你返回将所有点连接的最小总费用。只有任意两点之间 有且仅有一条简单路径时，才认为所有点都已连接。

示例 1：
输入：points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
输出：20
解释：

我们可以按照上图所示连接所有点得到最小总费用，总费用为 20 。
注意到任意两个点之间只有唯一一条路径互相到达。

示例 2：
输入：points = [[3,12],[-2,5],[-4,1]]
输出：18

示例 3：
输入：points = [[0,0],[1,1],[1,0],[-1,1]]
输出：4

示例 4：
输入：points = [[-1000000,-1000000],[1000000,1000000]]
输出：4000000

示例 5：
输入：points = [[0,0]]
输出：0

提示：

1 <= points.length <= 1000
-106<= xi, yi <= 106
所有点(xi, yi)两两不同。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/min-cost-to-connect-all-points
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class UnionSet:
    def __init__(self, n):
        self.n = n
        self.rank = [1] * n
        self.f = [i for i in range(n)]

    def find(self, x):
        if self.f[x] == x:
            return x
        self.f[x] = self.find(self.f[x])
        return self.f[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False

        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x

        self.rank[root_x] += self.rank[root_y]
        self.f[root_y] = root_x
        return True


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """
        根据题意，我们得到了一张 n 个节点的完全图，任意两点之间的距离均为它们的曼哈顿距离。
        现在我们需要在这个图中取得一个子图，恰满足子图的任意两点之间有且仅有一条简单路径，
        且这个子图的所有边的总权值之和尽可能小。

        能够满足任意两点之间有且仅有一条简单路径只有树，且这棵树包含 n 个节点。
        我们称这棵树为给定的图的生成树，其中总权值最小的生成树，我们称其为最小生成树。

        最小生成树有一个非常经典的解法：Kruskal。

        方法一：Kruskal 算法
        思路及解法
        Kruskal 算法是一种常见并且好写的最小生成树算法，由Kruskal 发明。
        该算法的基本思想是从小到大加入边，是一个贪心算法。
        其算法流程为：
        将图G={V,E} 中的所有边按照长度由小到大进行排序，等长的边可以按任意顺序。
        初始化图 G'为{V,∅}，从前向后扫描排序后的边，如果扫描到的边 e 在 G'中连接了两个相异的连通块,则将它插入 G'中。

        最后得到的图 G'就是图 G 的最小生成树。

        在实际代码中，我们首先将这张完全图中的边全部提取到边集数组中，
        然后对所有边进行排序，从小到大进行枚举，每次贪心选边加入答案。
        使用并查集维护连通性，若当前边两端不连通即可选择这条边。

        作者：LeetCode-Solution
        链接：https://leetcode-cn.com/problems/min-cost-to-connect-all-points/solution/lian-jie-suo-you-dian-de-zui-xiao-fei-yo-kcx7/
        来源：力扣（LeetCode）
        著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        """
        dist = lambda x, y: abs(points[x][0] - points[y][0]) + abs(points[x][1] - points[y][1])

        n = len(points)
        dsu = UnionSet(n)
        edges = list()

        for i in range(n):
            for j in range(i + 1, n):
                edges.append((dist(i, j), i, j))

        edges.sort()

        ret, num = 0, 1
        for length, x, y in edges:
            if dsu.union(x, y):
                ret += length
                num += 1
                if num == n:
                    break

        return ret


if __name__ == '__main__':
    s = Solution()
    print(s.minCostConnectPoints([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]))
    print(s.minCostConnectPoints([[-1000000, -1000000], [1000000, 1000000]]))
