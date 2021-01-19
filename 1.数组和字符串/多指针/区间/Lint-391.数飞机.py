"""
描述
给出飞机的起飞和降落时间的列表，用序列 interval 表示. 请计算出天上同时最多有多少架飞机？

说明
如果多架飞机降落和起飞在同一时刻，我们认为降落有优先权。

样例
- 样例 1:

输入: [(1, 10), (2, 3), (5, 8), (4, 7)]
输出: 3
解释:
第一架飞机在1时刻起飞, 10时刻降落.
第二架飞机在2时刻起飞, 3时刻降落.
第三架飞机在5时刻起飞, 8时刻降落.
第四架飞机在4时刻起飞, 7时刻降落.
在5时刻到6时刻之间, 天空中有三架飞机.

- 样例 2:

输入: [(1, 2), (2, 3), (3, 4)]
输出: 1
解释: 降落优先于起飞.
"""


class Solution:
    def countOfAirplanes(self, airplanes):
        # Write your code here
        room = []
        # 加入开始时间和结束时间，1是房间+1，-1是房间-1
        for i in airplanes:
            room.append((i[0], 1))
            room.append((i[1], -1))
        tmp = 0
        ans = 0
        # 排序
        room = sorted(room)
        # 扫描一遍
        for idx, cost in room:
            tmp += cost
            ans = max(ans, tmp)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.countOfAirplanes([(1, 10), (2, 3), (5, 8), (4, 7)]))
