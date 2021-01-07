"""
给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。
注意:

可以认为区间的终点总是大于它的起点。
区间 [1,2] 和 [2,3] 的边界相互“接触”，但没有相互重叠。

示例 1:
输入: [ [1,2], [2,3], [3,4], [1,3] ]
输出: 1
解释: 移除 [1,3] 后，剩下的区间没有重叠。

示例 2:
输入: [ [1,2], [1,2], [1,2] ]
输出: 2
解释: 你需要移除两个 [1,2] 来使剩下的区间没有重叠。

示例 3:
输入: [ [1,2], [2,3] ]
输出: 0
解释: 你不需要移除任何区间，因为它们已经是无重叠的了。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/non-overlapping-intervals
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    # 方法一，排序+贪心，88 ms，51.97%
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        类似在学校参加活动，按最先结束的排序来安排日程表，以便参加最多的活动
        """
        # 排序的lambda写法
        intervals.sort(key=lambda x: x[1])
        schedule = []
        for inter in intervals:
            if not schedule or schedule[-1][1] <= inter[0]:
                schedule.append(inter)
        return len(intervals) - len(schedule)


if __name__ == '__main__':
    s = Solution()
    print(s.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]))
    print(s.eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]))
    print(s.eraseOverlapIntervals([[1, 2], [2, 3]]))
    # 空数组
    print(s.eraseOverlapIntervals([]))
    # 单数组
    print(s.eraseOverlapIntervals([[1, 2]]))
