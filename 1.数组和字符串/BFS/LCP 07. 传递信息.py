"""
小朋友 A 在和 ta 的小伙伴们玩传信息游戏，游戏规则如下：

有 n 名玩家，所有玩家编号分别为 0 ～ n-1，其中小朋友 A 的编号为 0
每个玩家都有固定的若干个可传信息的其他玩家（也可能没有）。
传信息的关系是单向的（比如 A 可以向 B 传信息，但 B 不能向 A 传信息）。
每轮信息必须需要传递给另一个人，且信息可重复经过同一个人
给定总玩家数 n，以及按 [玩家编号,对应可传递玩家编号] 关系组成的二维数组 relation。
返回信息从小 A (编号 0 ) 经过 k 轮传递到编号为 n-1 的小伙伴处的方案数；若不能到达，返回 0。

示例 1：

输入：n = 5, relation = [[0,2],[2,1],[3,4],[2,3],[1,4],[2,0],[0,4]], k = 3

输出：3

解释：信息从小 A 编号 0 处开始，经 3 轮传递，到达编号 4。共有 3 种方案，
分别是 0->2->0->4， 0->2->1->4， 0->2->3->4。

示例 2：

输入：n = 3, relation = [[0,2],[2,1]], k = 2

输出：0

解释：信息不能从小 A 处经过 2 轮传递到编号 2

限制：

2 <= n <= 10
1 <= k <= 5
1 <= relation.length <= 90, 且 relation[i].length == 2
0 <= relation[i][0],relation[i][1] < n 且 relation[i][0] != relation[i][1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/chuan-di-xin-xi
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
from collections import defaultdict
from typing import List


class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        ways = defaultdict(list)
        for way in relation:
            ways[way[0]].append(way[1])
        # print(ways)
        stack = [0]
        while k > 0:
            temp = stack.copy()
            stack.clear()
            for site in temp:
                stack.extend(ways[site])
            k -= 1
        return stack.count(n - 1)


class Solution:
    """
    方法一：深度优先搜索
    可以把传信息的关系看成有向图，每个玩家对应一个节点，每个传信息的关系对应一条有向边。
    如果 x 可以向 y 传信息，则对应从节点 x 到节点 y 的一条有向边。
    寻找从编号 0 的玩家经过 k 轮传递到编号 n-1 的玩家处的方案数，
    等价于在有向图中寻找从节点 0 到节点 n-1的长度为 k 的路径数，同一条路径可以重复经过同一个节点。

    可以使用深度优先搜索计算方案数。从节点 0 出发做深度优先搜索，
    每一步记录当前所在的节点以及经过的轮数，当经过 k 轮时，如果位于节点 n-1，则将方案数加 1。
    搜索结束之后，即可得到总的方案数。

    具体实现方面，可以对传信息的关系进行预处理，使用列表存储有向边的关系，
    即可在 O(1) 的时间内得到特定节点的相邻节点（即可以沿着有向边一步到达的节点）。

    作者：LeetCode-Solution
    链接：https://leetcode-cn.com/problems/chuan-di-xin-xi/solution/chuan-di-xin-xi-by-leetcode-solution/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def numWays(self, n: int, relation: List[int], k: int) -> int:
        self.ways, self.n, self.k = 0, n, k
        self.edges = collections.defaultdict(list)
        for src, dst in relation:
            self.edges[src].append(dst)

        self.dfs(0, 0)
        return self.ways

    def dfs(self, index, steps):
        if steps == self.k:
            if index == self.n - 1:
                self.ways += 1
            return
        for to in self.edges[index]:
            self.dfs(to, steps + 1)


class Solution:
    """
    方法二：广度优先搜索
    也可以使用广度优先搜索计算方案数。从节点 00 出发做广度优先搜索，当遍历到 kk 层时，如果位于节点 n-1n−1，则将方案数加 11。搜索结束之后，即可得到总的方案数。

    作者：LeetCode-Solution
    链接：https://leetcode-cn.com/problems/chuan-di-xin-xi/solution/chuan-di-xin-xi-by-leetcode-solution/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def numWays(self, n: int, relation: List[int], k: int) -> int:
        edges = collections.defaultdict(list)
        for edge in relation:
            src = edge[0]
            dst = edge[1]
            edges[src].append(dst)
        steps = 0
        queue = collections.deque([0])
        while queue and steps < k:
            steps += 1
            size = len(queue)
            for i in range(size):
                index = queue.popleft()
                to = edges[index]
                for nextIndex in to:
                    queue.append(nextIndex)
        ways = 0
        if steps == k:
            while queue:
                if queue.popleft() == n - 1:
                    ways += 1
        return ways


if __name__ == '__main__':
    s = Solution()
    print(s.numWays(n=5, relation=[[0, 2], [2, 1], [3, 4], [2, 3], [1, 4], [2, 0], [0, 4]], k=3))
    print(s.numWays(n=3, relation=[[0, 2], [2, 1]], k=2))
