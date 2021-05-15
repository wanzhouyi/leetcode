"""
节点间通路。给定有向图，设计一个算法，找出两个节点之间是否存在一条路径。

示例1:

 输入：n = 3, graph = [[0, 1], [0, 2], [1, 2], [1, 2]], start = 0, target = 2
 输出：true
示例2:

 输入：n = 5, graph = [[0, 1], [0, 2], [0, 4], [0, 4], [0, 1], [1, 3], [1, 4], [1, 3], [2, 3], [3, 4]], start = 0, target = 4
 输出 true
提示：

节点数量n在[0, 1e5]范围内。
节点编号大于等于 0 小于 n。
图中可能存在自环和平行边。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/route-between-nodes-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def findWhetherExistsPath(self, n: int, graph: List[List[int]], start: int,
                              target: int) -> bool:
        from collections import defaultdict
        dic = defaultdict(set)
        for begin, end in graph:
            dic[begin].add(end)

        visited = set()

        def dfs(node):
            for nxt in dic[node]:
                if nxt == target:
                    return True
                if (node, nxt) not in visited:
                    if dfs(nxt):
                        return True
            return False

        return dfs(start)


class Solution:
    def findWhetherExistsPath(self, n: int, graph: List[List[int]], start: int,
                              target: int) -> bool:
        if start == target:
            return True
        for line in graph:
            if line[1] == target:
                return self.findWhetherExistsPath(n, graph, start, line[0])
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.findWhetherExistsPath(n=3, graph=[[0, 1], [0, 2], [1, 2], [1, 2]], start=0, target=2))
    print(s.findWhetherExistsPath(n=5,
                                  graph=[[0, 1], [0, 2], [0, 4], [0, 4], [0, 1], [1, 3], [1, 4],
                                         [1, 3], [2, 3], [3, 4]], start=0, target=4))
