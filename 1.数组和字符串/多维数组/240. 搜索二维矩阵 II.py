"""
编写一个高效的算法来搜索mxn矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：
每行的元素从左到右升序排列。
每列的元素从上到下升序排列。

示例 1：
输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
输出：true

示例 2：
输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
输出：false

提示：

m == matrix.length
n == matrix[i].length
1 <= n, m <= 300
-109<= matix[i][j] <= 109
每行的所有元素从左到右升序排列
每列的所有元素从上到下升序排列
-109<= target <= 109

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-a-2d-matrix-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    # 方法一，模拟，2164ms，5.77%
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        stack = {(0, 0)}
        while stack:
            x, y = stack.pop()
            if matrix[x][y] == target:
                return True
            else:
                for x0, y0 in [(0, 1), (1, 0)]:
                    new_x, new_y = x + x0, y + y0
                    if new_x < m and new_y < n:
                        stack.add((new_x, new_y))
        return False

    # 方法一的优化，276 ms，5.77%
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        visited = set()
        stack = {(0, 0)}
        while stack:
            x, y = stack.pop()
            visited.add((x, y))
            if matrix[x][y] == target:
                return True
            else:
                for x0, y0 in [(0, 1), (1, 0)]:
                    new_x, new_y = x + x0, y + y0
                    if new_x < m and new_y < n and (new_x, new_y) not in visited:
                        stack.add((new_x, new_y))
        return False

    # 方法三，二分查找，208 ms，15%
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        import bisect
        for idx, row in enumerate(matrix):
            tar_idx = bisect.bisect_right(row, target)
            if tar_idx > 0 and row[tar_idx - 1] == target:
                return True
        return False

    # 官解
    def searchMatrix(self, matrix, target):
        # an empty matrix obviously does not contain `target` (make this check
        # because we want to cache `width` for efficiency's sake)
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        # cache these, as they won't change.
        height = len(matrix)
        width = len(matrix[0])

        # start our "pointer" in the bottom-left
        row = height - 1
        col = 0

        while col < width and row >= 0:
            if matrix[row][col] > target:
                row -= 1
            elif matrix[row][col] < target:
                col += 1
            else:  # found it
                return True

        return False


if __name__ == '__main__':
    s = Solution()
    print(s.searchMatrix(
        matrix=[[1, 4, 7, 11, 15],
                [2, 5, 8, 12, 19],
                [3, 6, 9, 16, 22],
                [10, 13, 14, 17, 24],
                [18, 21, 23, 26, 30]], target=29))
