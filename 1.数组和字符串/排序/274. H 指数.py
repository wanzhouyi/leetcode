"""
给定一位研究者论文被引用次数的数组（被引用次数是非负整数）。编写一个方法，计算出研究者的 h指数。
h 指数的定义：h 代表“高引用次数”（high citations），一名科研人员的 h 指数是指他（她）的 （N 篇论文中）总共有 h 篇论文分别被引用了至少 h 次。且其余的N - h篇论文每篇被引用次数不超过 h 次。
例如：某人的 h 指数是 20，这表示他已发表的论文中，每篇被引用了至少 20 次的论文总共有 20 篇。
示例：
输入：citations = [3,0,6,1,5]
输出：3 
解释：给定数组表示研究者总共有 5 篇论文，每篇论文相应的被引用了 3, 0, 6, 1, 5 次。
    由于研究者有 3 篇论文每篇 至少 被引用了 3 次，其余两篇论文每篇被引用 不多于 3 次，所以她的 h 指数是 3。

提示：如果 h 有多种可能的值，h 指数是其中最大的那个。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/h-index
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        print(citations)
        n = len(citations)
        ans = 0
        for i in range(n):
            if citations[i] >= i + 1:
                ans = max(ans, i + 1)
        return ans


class Solution:
    """
    首先我们可以将初始的H 指数 h 设为 0，然后将引用次数排序，并且对排序后的数组从大到小遍历。

    根据H 指数的定义，如果当前H 指数为 h 并且在遍历过程中找到当前值 citations[i]>h，
    则说明我们找到了一篇被引用了至少 h+1 次的论文，所以将现有的 h 值加 1。继续遍历直到 h 无法继续增大。
    最后返回 h 作为最终答案。

    作者：LeetCode-Solution
    链接：https://leetcode-cn.com/problems/h-index/solution/h-zhi-shu-by-leetcode-solution-fnhl/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def hIndex(self, citations: List[int]) -> int:
        sorted_citation = sorted(citations, reverse=True)
        h = 0
        i = 0
        n = len(citations)
        while i < n and sorted_citation[i] > h:
            h += 1
            i += 1
        return h


if __name__ == '__main__':
    s = Solution()
    print(s.hIndex([3, 0, 6, 1, 5]))
    print(s.hIndex([0]))
    print(s.hIndex([0, 0]))
    print(s.hIndex([0, 1]))
    print(s.hIndex([9]))
    print(s.hIndex([9, 9]))

    print(s.hIndex([4, 4, 0, 0]))
