"""
在一个XY 坐标系中有一些点，我们用数组coordinates来分别记录它们的坐标，
其中coordinates[i] = [x, y]表示横坐标为 x、纵坐标为 y的点。
请你来判断，这些点是否在该坐标系中属于同一条直线上，是则返回 true，否则请返回 false。

示例 1：
输入：coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
输出：true

示例 2：
输入：coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
输出：false
提示：

2 <=coordinates.length <= 1000
coordinates[i].length == 2
-10^4 <=coordinates[i][0],coordinates[i][1] <= 10^4
coordinates中不含重复的点

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/check-if-it-is-a-straight-line
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    # 方法一，数学法，72ms，21.52%
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        """
        注意除数不能为0
        """
        # 先计算斜率
        x0, y0 = coordinates[0][0], coordinates[0][1]
        x1, y1 = coordinates[1][0], coordinates[1][1]
        n = len(coordinates)
        if x1 == x0:
            for i in range(2, n):
                if coordinates[i][0] != x0:
                    return False
        else:
            slope = (y1 - y0) / (x1 - x0)
            for i in range(2, n):
                xi, yi = coordinates[i][0], coordinates[i][1]
                if xi == x0:
                    return False
                if (yi - y0) / (xi - x0) != slope:
                    return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.checkStraightLine(coordinates=[[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]))
    print(s.checkStraightLine(coordinates=[[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]))
