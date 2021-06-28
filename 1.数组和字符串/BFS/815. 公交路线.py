"""
给你一个数组 routes ，表示一系列公交线路，其中每个 routes[i] 表示一条公交线路，第 i 辆公交车将会在上面循环行驶。

例如，路线 routes[0] = [1, 5, 7] 表示第 0 辆公交车会一直按序列 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... 这样的车站路线行驶。
现在从 source 车站出发（初始时不在公交车上），要前往 target 车站。 期间仅可乘坐公交车。

求出 最少乘坐的公交车数量 。如果不可能到达终点车站，返回 -1 。



示例 1：

输入：routes = [[1,2,7],[3,6,7]], source = 1, target = 6
输出：2
解释：最优策略是先乘坐第一辆公交车到达车站 7 , 然后换乘第二辆公交车到车站 6 。 
示例 2：

输入：routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12
输出：-1


提示：

1 <= routes.length <= 500.
1 <= routes[i].length <= 105
routes[i] 中的所有值 互不相同
sum(routes[i].length) <= 105
0 <= routes[i][j] < 106
0 <= source, target < 106

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/bus-routes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        m = len(routes)
        from collections import defaultdict
        dic = defaultdict(list)
        for i in range(m):
            for num in routes[i]:
                dic[num].append(i)

        stack = {source}
        visited = set()
        cnt = 0
        while stack:
            cnt += 1
            temp = stack.copy()
            stack.clear()
            for num in temp:
                if num == target:
                    return cnt - 1
                for idx in dic[num]:
                    if idx not in visited:
                        stack = stack.union(set(routes[idx]))
                        visited.add(idx)
        return -1


from collections import deque
from typing import List
import sys


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        routes_count = len(routes)
        # station_map用来存储每个站点上的公交线路，相当于生活中每个公交站点的公交站牌
        # key：站点 val：一个列表，该站点能乘坐的所有公交路线
        station_map = dict()
        for route in range(routes_count):
            for station in routes[route]:
                if station in station_map:
                    station_map[station].append(route)
                else:
                    station_map.update({station: [route]})

        starts = deque()  # starts用来存储所有的起始位置
        for route in range(routes_count):
            if source in routes[route]:
                starts.append(route)

        min_step = sys.maxsize
        while starts:  # 遍历起点然后进行BFS
            start = starts.popleft()
            visited = set()
            visited.add(start)
            q = deque()
            q.append(start)
            step = 1

            while q:
                for _ in range(len(q)):
                    route = q.popleft()

                    if target in routes[route]:
                        min_step = min(min_step, step)  # 记录最小换乘次数
                        break  # 这里是break，不是return，因为还有其他起点没有遍历
                    for station in routes[route]:
                        for next_route in station_map[station]:
                            if next_route not in visited:
                                q.append(next_route)
                                visited.add(next_route)

                step += 1

        return min_step if min_step != sys.maxsize else -1
