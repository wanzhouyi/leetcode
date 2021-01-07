"""
n皇后问题 研究的是如何将 n个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
给你一个整数 n ，返回所有不同的n皇后问题 的解决方案。
每一种解法包含一个不同的n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

示例 1：
输入：n = 4
输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
解释：如上图所示，4 皇后问题存在两个不同的解法。

示例 2：
输入：n = 1
输出：[["Q"]]
提示：
1 <= n <= 9
皇后彼此不能相互攻击，也就是说：任何两个皇后都不能处于同一条横行、纵行或斜线上。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/n-queens
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        path = []

        def back_track(m, n, path):
            if n == 0:
                result.append(path.copy())
                return
            for i in range(m):  # 第几列
                if i in [x.index('Q') for x in path]: continue
                temp = any(list(map(lambda x: abs(x[0] - (m - n)) == abs(x[1] - i),
                                    [[row, val.index('Q')] for row, val in enumerate(path)])))
                if temp: continue

                path.append('.' * i + 'Q' + '.' * (m - i - 1))
                back_track(m, n - 1, path)
                path.pop()

        back_track(n, n, path)
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.solveNQueens(4))
