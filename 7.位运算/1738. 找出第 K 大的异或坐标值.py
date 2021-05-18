"""
给你一个二维矩阵 matrix 和一个整数 k ，矩阵大小为m x n 由非负整数组成。

矩阵中坐标 (a, b) 的 值 可由对所有满足 0 <= i <= a < m 且 0 <= j <= b < n 的元素 matrix[i][j]（下标从 0 开始计数）执行异或运算得到。

请你找出matrix 的所有坐标中第 k 大的值（k 的值从 1 开始计数）。



示例 1：

输入：matrix = [[5,2],[1,6]], k = 1
输出：7
解释：坐标 (0,1) 的值是 5 XOR 2 = 7 ，为最大的值。
示例 2：

输入：matrix = [[5,2],[1,6]], k = 2
输出：5
解释：坐标 (0,0) 的值是 5 = 5 ，为第 2 大的值。
示例 3：

输入：matrix = [[5,2],[1,6]], k = 3
输出：4
解释：坐标 (1,0) 的值是 5 XOR 1 = 4 ，为第 3 大的值。
示例 4：

输入：matrix = [[5,2],[1,6]], k = 4
输出：0
解释：坐标 (1,1) 的值是 5 XOR 2 XOR 1 XOR 6 = 0 ，为第 4 大的值。


提示：

m == matrix.length
n == matrix[i].length
1 <= m, n <= 1000
0 <= matrix[i][j] <= 106
1 <= k <= m * n

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-kth-largest-xor-coordinate-value
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        # 第一步：求出行数和列数
        m, n = len(matrix), len(matrix[0])
        # 第二步：构造一个新的数组，用于存放二维数组中当前的前缀异或的结果。
        # 注意这里多加了一行一列，便于后面进行求前缀异或
        new_matrix = [[0] * (n + 1) for _ in range(m + 1)]
        # 第三步：构建一个新的数组，用于存放所有的前缀异或结果
        arr_result = []
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 当前位置的前缀异或结果等于同行左边前缀、同列上方前缀、左上角前缀三个数据的异或结果
                new_matrix[i][j] = matrix[i - 1][j - 1] ^ \
                                   new_matrix[i - 1][j] ^ \
                                   new_matrix[i][j - 1] ^ \
                                   new_matrix[i - 1][j - 1]
                arr_result.append(new_matrix[i][j])
        arr_result.sort(reverse=True)
        return arr_result[k - 1]


if __name__ == '__main__':
    s = Solution()
    print(s.kthLargestValue(matrix=[[5, 2], [1, 6]], k=1))
    print(s.kthLargestValue([[8, 10, 5, 8, 5, 7, 6, 0, 1, 4, 10, 6, 4, 3, 6, 8, 7, 9, 4, 2]], 2))
