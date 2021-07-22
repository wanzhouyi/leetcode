"""
给你一个二维整数数组ranges和两个整数left和right。每个ranges[i] = [starti, endi]表示一个从starti到endi的闭区间。
如果闭区间[left, right]内每个整数都被ranges中至少一个区间覆盖，那么请你返回true，否则返回false。
已知区间 ranges[i] = [starti, endi] ，如果整数 x 满足 starti <= x <= endi，那么我们称整数x被覆盖了。

示例 1：
输入：ranges = [[1,2],[3,4],[5,6]], left = 2, right = 5
输出：true
解释：2 到 5 的每个整数都被覆盖了：
- 2 被第一个区间覆盖。
- 3 和 4 被第二个区间覆盖。
- 5 被第三个区间覆盖。
示例 2：
输入：ranges = [[1,10],[10,20]], left = 21, right = 21
输出：false
解释：21 没有被任何一个区间覆盖。

提示：

1 <= ranges.length <= 50
1 <= starti <= endi <= 50
1 <= left <= right <= 50

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/check-if-all-the-integers-in-a-range-are-covered
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        arr = [x for x in range(left, right + 1)]
        for ls in ranges:
            for num in range(ls[0], ls[1] + 1):
                try:
                    arr.remove(num)
                except ValueError:
                    pass
        return True if not arr else False


if __name__ == '__main__':
    s = Solution()
    print(s.isCovered(ranges=[[1, 2], [3, 4], [5, 6]], left=2, right=5))
    print(s.isCovered(ranges=[[1, 10], [10, 20]], left=21, right=21))
