"""
给你一个整数数组 nums ，返回 nums 中所有 等差子序列 的数目。
如果一个序列中 至少有三个元素 ，并且任意两个相邻元素之差相同，则称该序列为等差序列。
例如，[1, 3, 5, 7, 9]、[7, 7, 7, 7] 和 [3, -1, -5, -9] 都是等差序列。
再例如，[1, 1, 2, 5, 7] 不是等差序列。
数组中的子序列是从数组中删除一些元素（也可能不删除）得到的一个序列。

例如，[2,5,10] 是 [1,2,1,2,4,1,5,10] 的一个子序列。
题目数据保证答案是一个 32-bit 整数。

示例 1：

输入：nums = [2,4,6,8,10]
输出：7
解释：所有的等差子序列为：
[2,4,6]
[4,6,8]
[6,8,10]
[2,4,6,8]
[4,6,8,10]
[2,4,6,8,10]
[2,6,10]
示例 2：

输入：nums = [7,7,7,7,7]
输出：16
解释：数组中的任意子序列都是等差子序列。

提示：

1 <= nums.length <= 1000
-2^31 <= nums[i] <= 2^31 - 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/arithmetic-slices-ii-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import bisect
import collections
from collections import defaultdict
from typing import List

from functools import lru_cache


class Solution:
    # 不用动态规划的解法
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        # 第一步：将数组中的元素放入字典中，加快搜索速度。
        # 其中，key为数值，value是一个数组，存放的是数值的索引
        dic = dict()
        for idx, num in enumerate(nums):
            if num in dic:
                dic[num].append(idx)
            else:
                dic.setdefault(num, [idx])

        # 第二步， 构造递归函数
        # 这里使用了lru_cache，帮助快速返回目标值
        # 三个参数，cha表示当前等差数列的差，nxt_idx代表当前元素的索引，nxt_num代表当前元素的数值
        @lru_cache(None)
        def cal(cha: int, nxt_idx: int, nxt_num: int):
            # 如果查找的值在字典中，则进入下一步，否则直接返回0
            if nxt_num in dic:
                # 当前值的个数，就是字典里当前值的数组长度
                node_len = len(dic[nxt_num])
                # 通过二分查找，找到有多少个数值可以加入当前序列中
                valid_index = bisect.bisect_right(dic[nxt_num], nxt_idx)
                valid_cnt = node_len - valid_index
                # 如果当前可用个数大于0，代表有新值可以加入到序列中
                if valid_cnt > 0:
                    # 分别以每一个数值为起点，计算下一步
                    for index in dic[nxt_num][valid_index:]:
                        # 这里的加法是这样理解，比如[1,2,3,3],当前值是2，下一个元素有两种取法，则结果是2
                        valid_cnt += cal(cha, index, nxt_num + cha)
                    return valid_cnt
                else:
                    return 0
            else:
                return 0

        n = len(nums)
        ans = 0
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                cha = nums[j] - nums[i]
                nxt_num = nums[j] + cha
                nxt_idx = j
                ans += cal(cha, nxt_idx, nxt_num)
        # print(cnt)
        return ans


# 官解
class Solution:
    """
    方法一：动态规划 + 哈希表
    我们首先考虑至少有两个元素的等差子序列，下文将其称作弱等差子序列。

    由于尾项和公差可以确定一个等差数列，因此我们定义状态 f[i][d]表示尾项为 nums[i]，公差为 d 的弱等差子序列的个数。

    我们用一个二重循环去遍历 nums 中的所有元素对 (nums[i],nums[j])，其中 j<i。
    将 nums[i] 和nums[j] 分别当作等差数列的尾项和倒数第二项，则该等差数列的公差 d=nums[i]−nums[j]。
    由于公差相同，我们可以将 nums[i] 加到以 nums[j] 为尾项，公差为 d 的弱等差子序列的末尾，
    这对应着状态转移 f[i][d] += f[j][d]。
    同时，(nums[i],nums[j]) 这一对元素也可以当作一个弱等差子序列，故有状态转移
    f[i][d] += f[j][d] + 1

    由于题目要统计的等差子序列至少有三个元素，我们回顾上述二重循环，其中「将 nums[i] 加到以 nums[j] 为尾项，
    公差为 d 的弱等差子序列的末尾」这一操作，实际上就构成了一个至少有三个元素的等差子序列，
    因此我们将循环中的 f[j][d] 累加，即为答案。

    代码实现时，由于nums[i] 的范围很大，所以计算出的公差的范围也很大，我们可以将状态转移数组 f 的第二维用哈希表代替。

    作者：LeetCode-Solution
    链接：https://leetcode-cn.com/problems/arithmetic-slices-ii-subsequence/solution/deng-chai-shu-lie-hua-fen-ii-zi-xu-lie-b-77pl/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        ans = 0
        f = [defaultdict(int) for _ in nums]
        for i, x in enumerate(nums):
            for j in range(i):
                d = x - nums[j]
                cnt = f[j][d]
                ans += cnt
                f[i][d] += cnt + 1
        return ans


class Solution(object):
    """
    题意
    子序列：顺序不变的情况下，从数组中抽出来的一个序列；可以是不连续的。
    题目要求的是在数组中有多少个可以构成等差数列的子序列。

    解题思路
    本题是昨天每日一题 413. 等差数列划分 的拓展题。413 题要求的是可以构成等差数列的子数组（连续）的个数，
    本题换成了子序列（不连续）。
    我见到子序列问题，就想到了经典的题目：300. 最长递增子序列。也就是想起来了动态规划，
    本题和 300 题的动态规划的思路是相通的。
    先从整体思路说起。
    子序列问题，由于是数组中的非连续的一个序列，使用动态规划求解时，避免不了二重循环：
    第一重循环是求解动态规划的每一个状态 dp[i], (0 <= i <= N) ，
    第二重循环是向前寻找上一个子序列的结尾 j ,(0 <= j < i) 来和 i 一起构成满足题意的新的子序列。

    对于「最长递增子序列」问题，我们对 i, j 的要求是 nums[i] > nums[j]，即递增；
    对于「能构成等差数列的子序列」问题，我们对 i, j的要求是 num[i] 可以在 nums[j]的基础上构成等差数列。
    在动态规划问题中，我们找到一个符合条件的 j ，然后就可以通过状态转移方程由 dp[j] 推导出 dp[i]。

    然后，我理一下本题的解法。
    两重循环：外部循环用于计算每个 i 位置的状态，内部循环用于寻找符合条件的 j。
    何为符合条件？
    令等差数列的公差 diff = nums[i] - nums[j]，如果 nums[j] 是一个公差为 diff 的等差数列的结尾数字，
    则 nums[j] 符合条件。
    状态定义？
    在上面的分析中，我们看到对于 j 位置会有多个 diff ，所以一维的状态转移方程已经不够用了。
    必须定义两维的状态 dp[i][diff]，但是由于 diff的取值范围很大，所以不能用二维数组。
    最终定义两位的状态是 dp[i] - > dict，其含义是在 i 位置，以 diff为公差的、且以 nums[i] 为结尾元素的
    等差数列的个数为 dp[i][diff] - 1。 为什么要减一，见李威威的题解。
    状态转移方程？
    当寻找到了一个 j 符合条件时，相当于在长度为 dp[j][diff] 的递增子序列的尾部增加了一个元素 nums[i]，
    所以以 diff 为公差的、且以 nums[i] 为结尾元素的等差数列的个数为 dp[i][diff] += dp[j][diff] + 1
    结果？
    题目要求的结果是所有能形成等差数列的子序列的个数，所以结果是累加所有的状态。
    这时候注意要加的是 dp[j][diff]，因为只有 j 位置也出现了同样的 diff 的时候，才会和 i 一起形成长度 > 3 的等差数列。

    作者：fuxuemingzhu
    链接：https://leetcode-cn.com/problems/arithmetic-slices-ii-subsequence/solution/fu-xue-ming-zhu-jie-mi-zi-xu-lie-dong-ta-gepk/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def numberOfArithmeticSlices(self, nums):
        N = len(nums)
        dp = [collections.defaultdict(int) for i in range(N)]
        res = 0
        for i in range(N):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] += dp[j][diff] + 1
                if dp[j][diff]:
                    res += dp[j][diff]
        return res


if __name__ == '__main__':
    s = Solution()
    # print(s.numberOfArithmeticSlices(nums=[2, 4, 6, 8, 10]))
    print(s.numberOfArithmeticSlices(nums=[2, 4, 6, 6, 8, 10]))
    # print(s.numberOfArithmeticSlices(nums=[7, 7, 7, 7, 7]))
    print(s.numberOfArithmeticSlices(nums=[7] * 1000))
