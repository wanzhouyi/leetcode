"""
给你一个大小为m* n的矩阵mat，矩阵由若干军人和平民组成，分别用 1 和 0 表示。
请你返回矩阵中战斗力最弱的k行的索引，按从最弱到最强排序。
如果第i行的军人数量少于第j行，或者两行军人数量相同但 i 小于 j，那么我们认为第 i 行的战斗力比第 j 行弱。
军人 总是 排在一行中的靠前位置，也就是说 1 总是出现在 0 之前。
示例 1：
输入：mat =
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 
k = 3
输出：[2,0,3]
解释：
每行中的军人数目：
行 0 -> 2 
行 1 -> 4 
行 2 -> 1 
行 3 -> 2 
行 4 -> 5 
从最弱到最强对这些行排序后得到 [2,0,3,1,4]
示例 2：
输入：mat =
[[1,0,0,0],
[1,1,1,1],
[1,0,0,0],
[1,0,0,0]], 
k = 2
输出：[0,2]
解释： 
每行中的军人数目：
行 0 -> 1 
行 1 -> 4 
行 2 -> 1 
行 3 -> 1 
从最弱到最强对这些行排序后得到 [0,2,3,1]


提示：

m == mat.length
n == mat[i].length
2 <= n, m <= 100
1 <= k <= m
matrix[i][j] 不是 0 就是 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/the-k-weakest-rows-in-a-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import heapq
from typing import List
from sortedcontainers import SortedDict


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        dic = SortedDict()
        for idx, row in enumerate(mat):
            sm = sum(row)
            if sm in dic:
                dic[sm].append(idx)
            else:
                dic.setdefault(sm, [idx])
        ans = []
        k1 = k
        while k > 0:
            ls_curr = dic.popitem(0)[1]
            ans.extend(ls_curr)
            k -= len(ls_curr)
        return ans[:k1]


# 官解
class Solution:
    """
    思路与算法

    题目描述中有一条重要的保证：
    军人总是排在一行中的靠前位置，也就是说 1 总是出现在 0 之前。

    因此，我们可以通过二分查找的方法，找出一行中最后的那个 1 的位置。如果其位置为 pos，
    那么这一行 1 的个数就为 pos+1。特别地，如果这一行没有 1，那么令 pos=−1。

    当我们得到每一行的战斗力后，我们可以将它们全部放入一个小根堆中，并不断地取出堆顶的元素 k 次，
    这样我们就得到了最弱的 k 行的索引。

    需要注意的是，如果我们依次将每一行的战斗力以及索引（因为如果战斗力相同，索引较小的行更弱，
    所以我们需要在小根堆中存放战斗力和索引的二元组）放入小根堆中，那么这样做的时间复杂度是 O(mlogm) 的。
    一种更好的方法是使用这 m 个战斗力值直接初始化一个小根堆，时间复杂度为O(m)。
    读者可以参考《算法导论》的 \text{6.3}6.3 节或者「堆排序中建堆过程时间复杂度 O(n)O(n) 怎么来的？」
    了解该过程时间复杂度的证明方法。

    作者：LeetCode-Solution
    链接：https://leetcode-cn.com/problems/the-k-weakest-rows-in-a-matrix/solution/fang-zhen-zhong-zhan-dou-li-zui-ruo-de-k-xing-by-l/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        m, n = len(mat), len(mat[0])
        power = list()
        for i in range(m):
            l, r, pos = 0, n - 1, -1
            while l <= r:
                mid = (l + r) // 2
                if mat[i][mid] == 0:
                    r = mid - 1
                else:
                    pos = mid
                    l = mid + 1
            power.append((pos + 1, i))

        heapq.heapify(power)
        ans = list()
        for i in range(k):
            ans.append(heapq.heappop(power)[1])
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.kWeakestRows(mat=
                         [[1, 1, 0, 0, 0],
                          [1, 1, 1, 1, 0],
                          [1, 0, 0, 0, 0],
                          [1, 1, 0, 0, 0],
                          [1, 1, 1, 1, 1]],
                         k=3))
