"""
给你一个整数数组nums 以及两个整数lower 和 upper 。
求数组中，值位于范围 [lower, upper] （包含lower和upper）之内的 区间和的个数 。
区间和S(i, j)表示在nums中，位置从i到j的元素之和，包含i和j(i ≤ j)。

示例 1：
输入：nums = [-2,5,-1], lower = -2, upper = 2
输出：3
解释：存在三个区间：[0,0]、[2,2] 和 [0,2] ，对应的区间和分别是：-2 、-1 、2 。
示例 2：

输入：nums = [0], lower = 0, upper = 0
输出：1

提示：

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
-105 <= lower <= upper <= 105
题目数据保证答案是一个 32 位 的整数

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-of-range-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from bisect import bisect, bisect_right, insort, bisect_left
from typing import List


class Solution:
    """
    使用前缀数组pre，然后每个前缀和pre[i]二分查找前面i−1个和的pre[i]−lower和rpre[i]−upper的位置得出区间和的数量，
    然后把pre[i]二分插入到数组中保持数组有序

    作者：fan-cai
    链接：https://leetcode-cn.com/problems/count-of-range-sum/solution/python3-6xing-dai-ma-jian-ji-qian-zhui-he-er-fen-c/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        res, pre, now = 0, [0], 0
        for n in nums:
            now += n
            res += bisect_right(pre, now - lower) - bisect_left(pre, now - upper)
            insort(pre, now)
        return res
