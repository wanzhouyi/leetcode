"""
给定一个包含m x n个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。
示例1:
输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
输出: [1,2,3,6,9,8,7,4,5]

示例2:
输入:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
输出: [1,2,3,4,8,12,11,10,9,5,6,7]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/spiral-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        m, n = len(matrix), len(matrix[0])
        direct = ['right', 'down', 'left', 'up']
        direct_mp = {'right': (0, 1), 'down': (1, 0), 'left': (0, -1),
                     'up': (-1, 0)}

        def get_next_point(current_direct, current_point):
            x1, y1 = direct_mp[current_direct]
            new_x, new_y = x1 + current_point[0], y1 + current_point[1]
            if 0 <= new_x <= m - 1 and 0 <= new_y <= n - 1 and (
                    new_x, new_y) not in visited:
                return current_direct, (new_x, new_y)
            else:
                next_direct = direct.index(current_direct) + 1 if direct.index(
                    current_direct) < 3 else 0
                x1, y1 = direct_mp[direct[next_direct]]
                new_x, new_y = x1 + current_point[0], y1 + current_point[1]

                return direct[next_direct], (new_x, new_y)

        current_direct = 'right'
        current_point = (0, 0)
        result = []
        visited = set()
        counter, target = 0, m * n
        while counter < target:
            counter += 1
            visited.add(current_point)
            result.append(matrix[current_point[0]][current_point[1]])
            current_direct, current_point = get_next_point(current_direct,
                                                           current_point)
        return result
