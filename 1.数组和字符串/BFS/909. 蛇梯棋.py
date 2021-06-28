"""
N x N 的棋盘board 上，按从1 到 N*N的数字给方格编号，编号 从左下角开始，每一行交替方向。
例如，一块 6 x 6 大小的棋盘，编号如下：
r 行 c 列的棋盘，按前述方法编号，棋盘格中可能存在 “蛇” 或 “梯子”；如果 board[r][c] != -1，那个蛇或梯子的目的地将会是 board[r][c]。
玩家从棋盘上的方格1 （总是在最后一行、第一列）开始出发。
每一回合，玩家需要从当前方格 x 开始出发，按下述要求前进：
选定目标方格：选择从编号 x+1，x+2，x+3，x+4，x+5，或者 x+6 的方格中选出一个目标方格 s ，目标方格的编号 <= N*N。
该选择模拟了掷骰子的情景，无论棋盘大小如何，你的目的地范围也只能处于区间 [x+1, x+6] 之间。
传送玩家：如果目标方格 S 处存在蛇或梯子，那么玩家会传送到蛇或梯子的目的地。否则，玩家传送到目标方格 S。
注意，玩家在每回合的前进过程中最多只能爬过蛇或梯子一次：就算目的地是另一条蛇或梯子的起点，你也不会继续移动。

返回达到方格 N*N 所需的最少移动次数，如果不可能，则返回 -1。

示例：
输入：[
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,35,-1,-1,13,-1],
[-1,-1,-1,-1,-1,-1],
[-1,15,-1,-1,-1,-1]]
输出：4
解释：
首先，从方格 1 [第 5 行，第 0 列] 开始。
你决定移动到方格 2，并必须爬过梯子移动到到方格 15。
然后你决定移动到方格 17 [第 3 行，第 5 列]，必须爬过蛇到方格 13。
然后你决定移动到方格 14，且必须通过梯子移动到方格 35。
然后你决定移动到方格 36, 游戏结束。
可以证明你需要至少 4 次移动才能到达第 N*N 个方格，所以答案是 4。

提示：

2 <= board.length = board[0].length<= 20
board[i][j]介于1和N*N之间或者等于-1。
编号为1的方格上没有蛇或梯子。
编号为N*N的方格上没有蛇或梯子。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/snakes-and-ladders
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from collections import deque
from typing import List


class Solution:
    """
    解答错误
    [[-1,-1],[-1,3]]
    """

    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        nn = n * n
        shadow = [[0] * n for _ in range(n)]
        shadow_cnt = 1
        for row in range(n):
            temp_row = []
            for j in range(n):
                if row % 2 == 0:
                    temp_row.append(shadow_cnt)
                else:
                    temp_row.insert(0, shadow_cnt)
                shadow_cnt += 1
            shadow[n - 1 - row] = temp_row

        def get_next_pos(target):
            if target % n == 0:
                a = target // n
            else:
                a = target // n + 1
            b = shadow[n - a].index(target)

            return (n - a, b)

        cnt = 0
        stack = {(n - 1, 0)}
        while True:
            temp_stack = stack.copy()
            stack.clear()
            for x, y in temp_stack:
                if shadow[x][y] == nn:
                    return cnt
                if board[x][y] == -1:
                    for i in range(1, 7):
                        if shadow[x][y] + i <= nn:
                            stack.add(get_next_pos(shadow[x][y] + i))
                else:
                    stack.add(get_next_pos(board[x][y]))
            cnt += 1


class Solution:
    """
    方法一：广度优先搜索
    我们可以将棋盘抽象成一个包含 N^2个节点的有向图，对于每个节点 x，
    若 x+i(1≤i≤6) 上没有蛇或梯子，则连一条从 x 到 x+i 的有向边；
    否则记蛇梯的目的地为 y，连一条从 x 到 y 的有向边。

    如此转换后，原问题等价于在这张有向图上求出从 1 到 N^2的最短路长度。

    对于该问题，我们可以使用广度优先搜索。
    将节点编号和到达该节点的移动次数作为搜索状态，顺着该节点的出边扩展新状态，直至到达终点 N^2，返回此时的移动次数。若无法到达终点则返回−1。

    代码实现时，我们可以用一个队列来存储搜索状态，初始时将起点状态 (1,0) 加入队列，表示当前位于起点 1，移动次数为 0。
    然后不断取出队首，每次取出队首元素时扩展新状态，即遍历该节点的出边，若出边对应节点未被访问，则将该节点和移动次数加一的结果作为新状态，加入队列。如此循环直至到达终点或队列为空。

    此外，我们需要计算出编号在棋盘中的对应行列，以便从board 中得到目的地。
    设编号为 id，由于每行有 n 个数字，其位于棋盘从下往上数的第(id−1)/n行，记作 rr。
    由于棋盘的每一行会交替方向，若 r 为偶数，则编号方向从左向右，列号为(id−1)mod n；
    若 r 为奇数，则编号方向从右向左，列号为 n−1−((id−1) mod n)。
    """

    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        def id2rc(idx: int) -> (int, int):
            r, c = (idx - 1) // n, (idx - 1) % n
            if r % 2 == 1:
                c = n - 1 - c
            return n - 1 - r, c

        vis = set()
        q = deque([(1, 0)])
        while q:
            idx, step = q.popleft()
            for i in range(1, 6 + 1):
                idx_nxt = idx + i
                if idx_nxt > n * n:  # 超出边界
                    break

                x_nxt, y_nxt = id2rc(idx_nxt)  # 得到下一步的行列
                if board[x_nxt][y_nxt] > 0:  # 存在蛇或梯子
                    idx_nxt = board[x_nxt][y_nxt]
                if idx_nxt == n * n:  # 到达终点
                    return step + 1
                if idx_nxt not in vis:
                    vis.add(idx_nxt)
                    q.append((idx_nxt, step + 1))  # 扩展新状态

        return -1


if __name__ == '__main__':
    s = Solution()
    # print(s.snakesAndLadders([
    #     [-1, -1, -1, -1, -1, -1],
    #     [-1, -1, -1, -1, -1, -1],
    #     [-1, -1, -1, -1, -1, -1],
    #     [-1, 35, -1, -1, 13, -1],
    #     [-1, -1, -1, -1, -1, -1],
    #     [-1, 15, -1, -1, -1, -1]]))
    print(s.snakesAndLadders([[-1, -1],
                              [-1, 3]]))
