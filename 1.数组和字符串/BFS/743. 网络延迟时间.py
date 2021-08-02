"""
有 n 个网络节点，标记为1到 n。
给你一个列表times，表示信号经过 有向 边的传递时间。times[i] = (ui, vi, wi)，其中ui是源节点，vi是目标节点，
wi是一个信号从源节点传递到目标节点的时间。

现在，从某个节点K发出一个信号。需要多久才能使所有节点都收到信号？如果不能使所有节点收到信号，返回-1 。
示例 1：

输入：times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
输出：2
示例 2：

输入：times = [[1,2,1]], n = 2, k = 1
输出：1
示例 3：

输入：times = [[1,2,1]], n = 2, k = 2
输出：-1
提示：

1 <= k <= n <= 100
1 <= times.length <= 6000
times[i].length == 3
1 <= ui, vi <= n
ui != vi
0 <= wi <= 100
所有 (ui, vi) 对都 互不相同（即，不含重复边）

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/network-delay-time
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from collections import defaultdict, deque
from typing import List


class Solution:
    # 超时
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dic_edges = defaultdict(list)
        for u, v, t in times:
            dic_edges[u].append((v, t))

        dic_out_time = dict()

        def dfs(node: int, out_time: int):
            if node in dic_out_time:
                if dic_out_time[node] >= out_time:
                    dic_out_time[node] = out_time
                else:
                    return
            else:
                dic_out_time[node] = out_time

            for nxt_node, nxt_time in dic_edges[node]:
                dfs(nxt_node, out_time + nxt_time)

            return

        dfs(k, 0)
        if len(dic_out_time.keys()) == n:
            return max(dic_out_time.values())
        return -1

    # 错误
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dic_edges = defaultdict(list)
        dic_in = defaultdict(int)
        for u, v, t in times:
            dic_edges[u].append((v, t))
            dic_in[v] += 1
        dic_in[k] = 1
        dic_in_min = dict()
        visited = set()

        def dfs(node: int, out_time: int):
            if node not in dic_in_min:
                dic_in_min[node] = out_time
            else:
                dic_in_min[node] = min(dic_in_min[node], out_time)

            if dic_in[node] > 1:
                dic_in[node] -= 1
                return

            if node in visited:
                return
            visited.add(node)
            for nxt_node, nxt_time in dic_edges[node]:
                dfs(nxt_node, dic_in_min[node] + nxt_time)

            return

        dfs(k, 0)
        if len(dic_in_min.keys()) == n:
            return max(dic_in_min.values())
        return -1


class Solution:
    """
    简单递归的搜索一遍图，当然继续向下搜索的前提是遍历到某一结点的时间有所改善，不然没必要继续向下继续搜索了，不过其实 DFS 对于求最短路并不合适
    """

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """深度优先搜索"""
        # 建图 - 邻接表
        mp = [{} for i in range(n + 1)]
        for u, v, t in times:
            mp[u][v] = t
        # 记录结点最早收到信号的时间
        r = [-1 for i in range(n + 1)]

        def dfs(i: int, t: int) -> None:
            """在 t 时间到达 i 结点"""
            if r[i] == -1 or t < r[i]:
                r[i] = t
                for u, v in mp[i].items():
                    dfs(u, t + v)

        dfs(k, 0)

        minT = -1
        for i in range(1, n + 1):
            if r[i] == -1:
                return -1
            minT = max(minT, r[i])
        return minT


class Solution:
    """
    涉及最大最小的问题 BFS 显然比 DFS 更合适
    """

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """广度优先搜索"""
        # 建图 - 邻接表
        mp = [{} for i in range(n + 1)]
        for u, v, t in times:
            mp[u][v] = t
        # 记录结点最早收到信号的时间
        r = [-1 for i in range(n + 1)]
        r[k] = 0
        # 队列中存放 [结点，收到信号时间]
        s = deque([[k, 0]])
        while s:
            cur, t = s.popleft()
            for u, v in mp[cur].items():
                art = t + v
                # 仅当结点未收到或收到时间比记录时间更早才更新并入队
                if r[u] == -1 or art < r[u]:
                    r[u] = art
                    s.append([u, art])
        minT = -1
        for i in range(1, n + 1):
            if r[i] == -1:
                return -1
            minT = max(minT, r[i])
        return minT


if __name__ == '__main__':
    s = Solution()
    # print(s.networkDelayTime(times=[[2, 1, 1], [2, 3, 1], [3, 4, 1]], n=4, k=2))
    # print(s.networkDelayTime(times=[[2, 1, 1], [2, 3, 1], [3, 4, 1], [1, 4, 10]], n=4, k=2))
    print(s.networkDelayTime(times=[[2, 1, 1], [2, 3, 1], [3, 4, 1], [1, 4, 10], [4, 5, 3]], n=5,
                             k=2))
    # print(s.networkDelayTime(times=[[1, 2, 1]], n=2, k=1))
    # print(s.networkDelayTime(times=[[1, 2, 1]], n=2, k=2))
    # print(s.networkDelayTime(times=[[1, 2, 1], [2, 1, 3]], n=2, k=1))
    # print(s.networkDelayTime(times=[[1, 2, 1], [2, 3, 3], [3, 1, 5]], n=3, k=1))
    # print(s.networkDelayTime(
    #     [[3, 5, 78], [2, 1, 1], [1, 3, 0], [4, 3, 59], [5, 3, 85], [5, 2, 22], [2, 4, 23],
    #      [1, 4, 43], [4, 5, 75], [5, 1, 15], [1, 5, 91], [4, 1, 16], [3, 2, 98], [3, 4, 22],
    #      [5, 4, 31], [1, 2, 0], [2, 5, 4], [4, 2, 51], [3, 1, 36], [2, 3, 59]], 5, 5))
