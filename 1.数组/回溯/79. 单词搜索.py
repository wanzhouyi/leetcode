"""
给定一个二维网格和一个单词，找出该单词是否存在于网格中。
单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。
同一个单元格内的字母不允许被重复使用。

示例:
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
给定 word = "ABCCED", 返回 true
给定 word = "SEE", 返回 true
给定 word = "ABCB", 返回 false

提示：
board 和 word 中只包含大写和小写英文字母。
1 <= board.length <= 200
1 <= board[i].length <= 200
1 <= word.length <= 10^3
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-search
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    # 回溯，352 ms，15%
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        if not board or not board[0]:
            return False
        m, n = len(board), len(board[0])

        def back_track(x, y, chars, visited):
            if not chars or (x, y) in visited:
                return False

            if chars[0] == board[x][y]:
                visited.append((x, y))
                if len(visited) == len(word):
                    return True
                for x0, y0 in directions:
                    x1, y1 = x + x0, y + y0
                    if 0 <= x1 <= m - 1 and 0 <= y1 <= n - 1:
                        if back_track(x1, y1, chars[1:], visited):
                            return True
                visited.pop()
            return False

        for x in range(m):
            for y in range(n):
                if back_track(x, y, list(word), []):
                    return True
        return False
