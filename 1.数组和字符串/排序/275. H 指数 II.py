"""
给定一位研究者论文被引用次数的数组（被引用次数是非负整数），数组已经按照升序排列。编写一个方法，计算出研究者的 h 指数。
h 指数的定义: “h 代表“高引用次数”（high citations），一名科研人员的 h 指数是指他（她）的 （N 篇论文中）总共有 h 篇论文分别被引用了至少 h 次。（其余的N - h篇论文每篇被引用次数不多于 h 次。）"

示例:
输入: citations = [0,1,3,5,6]
输出: 3 
解释: 给定数组表示研究者总共有 5 篇论文，每篇论文相应的被引用了 0, 1, 3, 5, 6 次。
    由于研究者有 3 篇论文每篇至少被引用了 3 次，其余两篇论文每篇被引用不多于 3 次，所以她的 h 指数是 3。

说明:
如果 h 有多有种可能的值 ，h 指数是其中最大的那个。

进阶：

这是H 指数的延伸题目，本题中的citations数组是保证有序的。
你可以优化你的算法到对数时间复杂度吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/h-index-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        ans = 0
        if n == 1:
            return 0 if citations[0] == 0 else 1
        for i in range(n):
            if citations[i] >= n - i:
                ans = max(n - i, ans)
        return ans


class Solution:
    """
    方法一：二分查找
    由于数组 citations 已经按照升序排序，因此可以使用二分查找。

    设查找范围的初始左边界left 为 0, 初始右边界 right 为 n-1，其中 n 为数组 citations 的长度。
    每次在查找范围内取中点mid，则有 n−mid 篇论文被引用了至少citations[mid] 次。
    如果在查找过程中满足citations[mid]≥n−mid，则移动右边界right，否则移动左边界left。

    作者：LeetCode-Solution
    链接：https://leetcode-cn.com/problems/h-index-ii/solution/h-zhi-shu-ii-by-leetcode-solution-si7h/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        left = 0
        right = n - 1
        while left <= right:
            mid = left + (right - left) // 2
            if citations[mid] >= n - mid:
                right = mid - 1
            else:
                left = mid + 1
        return n - left
