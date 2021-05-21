"""
在两条独立的水平线上按给定的顺序写下 nums1 和 nums2 中的整数。

现在，可以绘制一些连接两个数字 nums1[i]和 nums2[j]的直线，这些直线需要同时满足满足：

nums1[i] == nums2[j]
且绘制的直线不与任何其他连线（非水平线）相交。
请注意，连线即使在端点也不能相交：每个数字只能属于一条连线。

以这种方法绘制线条，并返回可以绘制的最大连线数。



示例 1：


输入：nums1 = [1,4,2], nums2 = [1,2,4]
输出：2
解释：可以画出两条不交叉的线，如上图所示。 
但无法画出第三条不相交的直线，因为从 nums1[1]=4 到 nums2[2]=4 的直线将与从 nums1[2]=2 到 nums2[1]=2 的直线相交。
示例 2：

输入：nums1 = [2,5,1,2,5], nums2 = [10,5,2,1,5,2]
输出：3
示例 3：

输入：nums1 = [1,3,7,1,7,5], nums2 = [1,9,2,5,1]
输出：2


提示：

1 <= nums1.length <= 500
1 <= nums2.length <= 500
1 <= nums1[i], nums2[i] <= 2000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/uncrossed-lines
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
from functools import lru_cache


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        # 会超时，没优化出来
        set2 = set(nums2)
        ls_nums1 = []
        for num in nums1:
            if num in set2:
                ls_nums1.append(num)

        @lru_cache
        def dp(idx1: int, idx2: int):
            ls1 = ls_nums1[idx1:]
            ls2 = nums2[idx2:]
            if not ls1 or not ls2:
                return 0
            starter = ls1[0]
            # 不连
            ans = dp(idx1 + 1, idx2)
            # 连
            ct_starter = ls2.count(starter)
            if ct_starter > 0:
                starter_index = -1
                for i in range(ct_starter):
                    starter_index = ls2.index(starter, starter_index + 1)
                    ans = max(ans, dp(idx1 + 1, idx2 + starter_index + 1) + 1)
            return ans

        return dp(0, 0)


class Solution:
    """
    解题思路
    看到这个题目, 求最优解, 就想到用动态规划的思路来实现.
    两个数组nums1, nums2 求不交叉的连线数最大值, 考虑二维 dp 数组.

    定义
    dp[i][j]表示数组 nums1 的前 i 个数字和数组 nums2的前 j 个数字的能够形成不交叉连线的最大个数.
    其中 m 为 nums1 长度, n 为 nums2 长度.

    状态转移
    对于任意的 0 < i < m, 0 < j < n, 当 nums1[i]和 nums2[j] 字符相同的时候
    相比 dp[i-1][j-1]时, 当前的最大连线数又可以增加一条. 所以可以用 dp[i-1][j-1] + 1 来更新dp[i][j].
    如果字符不相等, 我们可以从 nums1 或者 num2 去掉一个字符进行比较.
    比如比较 dp[i-1][j]和 dp[i][j-1], 取两者中的较大值来更新 dp[i][j] 即可.
    dp[i-1][j] 代表不考虑 nums[i] 字符, nums[j]是考虑的, 但不是必须包含. dp[i][j−1] 同理
    最后, 遍历完成后, 结果在 dp[m][n] 上.
    总结
    这道题相比于 最长公共子序列（LCS)来说没有那么纯粹. 比较迷惑的地方是两个数组nums数字顺序不同, 会导致有交叉的情况不能计算在内.
    让我们直击本质, 忽略掉这些题目迷惑的地方. 不管给我们的数字是什么, 无非就是这两个点 可以连, 不可以连 两种状态.

    作者：niconiconi-12
    链接：https://leetcode-cn.com/problems/uncrossed-lines/solution/chi-xiao-dou-python-tu-wen-jian-ming-si-s7ukn/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        # 二维数组创建, 注意各个维度的创建顺序
        # dp 数组的处理上, 两个维度都各增加一位
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):

                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                # 因为 i, j 是相对dp数组来说的, 多加了一位, 因此读取 nums的时候要 -1
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)

        return dp[m][n]


if __name__ == '__main__':
    s = Solution()
    print(s.maxUncrossedLines(nums1=[1, 4, 2], nums2=[1, 2, 4]))
    print(s.maxUncrossedLines(nums1=[2, 5, 1, 2, 5], nums2=[10, 5, 2, 1, 5, 2]))
    print(s.maxUncrossedLines(nums1=[1, 3, 7, 1, 7, 5], nums2=[1, 9, 2, 5, 1]))
