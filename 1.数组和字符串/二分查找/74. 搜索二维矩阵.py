"""
编写一个高效的算法来判断m x n矩阵中，是否存在一个目标值。该矩阵具有如下特性：
每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。
示例 1：
输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
输出：true
示例 2：
输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
输出：false
提示：
m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 10^4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-a-2d-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
import bisect


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        col0 = [matrix[i][0] for i in range(len(matrix))]
        if target in col0:
            return True
        row_index = bisect.bisect_left(col0, target)
        row_index -= 1

        col_index = bisect.bisect_left(matrix[row_index], target)
        if col_index == len(matrix[0]):
            return False
        if matrix[row_index][col_index] == target:
            return True
        return False


# 负雪明烛
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        方法一：遍历
        该方法就是遍历查找每个位置，看 target 是否出现。这个方法也能通过本题。
        """
        M, N = len(matrix), len(matrix[0])
        for i in range(M):
            for j in range(N):
                if matrix[i][j] == target:
                    return True
        return False

    def searchMatrix(self, matrix, target):
        return any(target in row for row in matrix)

    def searchMatrix(self, matrix, target):
        """
        方法二：从左下角或者右上角开始查找
        这个方法是利用了矩阵的性质，如果我们从右上角开始遍历：
        如果要搜索的 target 比当前元素大，那么让行增加；
        如果要搜索的 target 比当前元素小，那么让列减小；
        """
        if not matrix or not matrix[0]:
            return False
        rows = len(matrix)
        cols = len(matrix[0])
        row, col = 0, cols - 1
        while True:
            if row < rows and col >= 0:
                if matrix[row][col] == target:
                    return True
                elif matrix[row][col] < target:
                    row += 1
                else:
                    col -= 1
            else:
                return False


class Solution(object):
    """
    方法四：两次二分查找
    这个方法可以说是方法三的改进。在方法三种，我们是先遍历找到 target 在哪一行，然后在该行遍历或者二分查找的 target 。其实也可以先用二分找到 target 所在的行，然后在该行二分找到 target。

    具体做法是，先找到 matrix[i][0] 小于 target 并且 matrix[i + 1][0] > target 的第 i 行，然后在该行内进行二分找到 target。

    作者：fuxuemingzhu
    链接：https://leetcode-cn.com/problems/search-a-2d-matrix/solution/fu-xue-ming-zhu-liu-chong-fang-fa-bang-n-e20z/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def searchMatrix(self, matrix, target):
        M, N = len(matrix), len(matrix[0])
        col0 = [row[0] for row in matrix]
        target_row = bisect.bisect_right(col0, target) - 1
        if target_row < 0:
            return False
        target_col = bisect.bisect_left(matrix[target_row], target)
        if target_col >= N:
            return False
        if matrix[target_row][target_col] == target:
            return True
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=66))
