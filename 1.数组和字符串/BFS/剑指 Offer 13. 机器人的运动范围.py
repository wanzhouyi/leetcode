"""
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。
一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），
也不能进入行坐标和列坐标的数位之和大于k的格子。
例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。
但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？



示例 1：

输入：m = 2, n = 3, k = 1
输出：3
示例 2：

输入：m = 3, n = 1, k = 0
输出：1
提示：

1 <= n,m <= 100
0 <= k<= 20

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def get_single_num(num):
            ans = 0
            while num > 10:
                num, yushu = divmod(num, 10)
                ans += yushu
            ans += num
            return ans

        visited = set()
        from collections import deque
        que = deque([(0, 0)])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while que:
            node = que.popleft()
            visited.add(node)
            for x, y in directions:
                new_x, new_y = node[0] + x, node[1] + y
                if 0 <= new_x <= m - 1 \
                        and 0 <= new_y <= n - 1 \
                        and get_single_num(new_x) + get_single_num(new_y) <= k \
                        and (new_x, new_y) not in visited:
                    que.append((new_x, new_y))
        return len(visited)


if __name__ == '__main__':
    s = Solution()
    # print(s.movingCount(m=2, n=3, k=1))
    # print(s.movingCount(m=2, n=3, k=0))
    # print(s.movingCount(m=3, n=1, k=0))
    print(s.movingCount(3, 2, 17))
