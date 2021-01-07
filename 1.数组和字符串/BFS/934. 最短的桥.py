"""
在给定的二维二进制数组A中，存在两座岛。（岛是由四面相连的 1 形成的一个最大组。）
现在，我们可以将0变为1，以使两座岛连接起来，变成一座岛。
返回必须翻转的0 的最小数目。（可以保证答案至少是 1。）

示例 1：
输入：[[0,1],[1,0]]
输出：1

示例 2：
输入：[[0,1,0],[0,0,0],[0,0,1]]
输出：2

示例 3：
输入：[[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
输出：1

提示：
1 <= A.length =A[0].length <= 100
A[i][j] == 0 或A[i][j] == 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shortest-bridge
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
from typing import List


class Solution(object):
    def shortestBridge(self, A):
        R, C = len(A), len(A[0])

        def neighbors(r, c):
            for nr, nc in ((r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)):
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc

        def get_components():
            done = set()
            components = []
            for r, row in enumerate(A):
                for c, val in enumerate(row):
                    if val and (r, c) not in done:
                        # Start dfs
                        stack = [(r, c)]
                        seen = {(r, c)}
                        while stack:
                            node = stack.pop()
                            for nei in neighbors(*node):
                                if A[nei[0]][nei[1]] and nei not in seen:
                                    stack.append(nei)
                                    seen.add(nei)
                        done |= seen
                        components.append(seen)
            return components

        source, target = get_components()
        print(source, target)
        queue = collections.deque([(node, 0) for node in source])
        done = set(source)
        while queue:
            node, d = queue.popleft()
            if node in target: return d - 1
            for nei in neighbors(*node):
                if nei not in done:
                    queue.append((nei, d + 1))
                    done.add(nei)


class Solution:
    def shortestBridge(self, nums):
        def dfs(i, j):  # 把找到的一个岛染成2，同时把找个岛的所有坐标放到队列q
            if i < 0 or i >= len(nums) or j < 0 or j >= len(nums[0]) or nums[i][j] == 0 or nums[i][
                j] == 2:  return
            if nums[i][j] == 1:
                nums[i][j] = 2
                q.append((i, j))
                for x, y in dirs:
                    newi, newj = x + i, y + j
                    dfs(newi, newj)

        def bfs(i, j):  # 从找到的岛开始扩展，每扩展一层，steps+1
            steps = 0
            while q:
                size = len(q)
                for _ in range(size):
                    i, j = q.popleft()
                    for x, y in dirs:
                        newi, newj = x + i, y + j
                        if newi < 0 or newi >= len(nums) or newj < 0 or newj >= len(nums[0]) or \
                                nums[newi][newj] == 2:  continue
                        if nums[newi][newj] == 1:  return steps
                        nums[newi][newj] = 2
                        q.append((newi, newj))
                steps += 1

        # main
        dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))
        q = collections.deque()
        for i, row in enumerate(nums):
            for j, ele in enumerate(row):
                if ele == 1:
                    dfs(i, j)
                    return bfs(i, j)


if __name__ == '__main__':
    s = Solution()
    print(s.shortestBridge([[0, 1], [1, 0]]))
    print(s.shortestBridge([[0, 1, 0], [0, 0, 0], [0, 0, 1]]))
    print(s.shortestBridge(
        [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 1, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]))
