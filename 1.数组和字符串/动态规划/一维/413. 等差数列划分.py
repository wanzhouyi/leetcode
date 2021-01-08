"""
如果一个数列至少有三个元素，并且任意两个相邻元素之差相同，则称该数列为等差数列。
例如，以下数列为等差数列:
1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
以下数列不是等差数列。
1, 1, 2, 5, 7
数组 A 包含 N 个数，且索引从0开始。数组 A 的一个子数组划分为数组 (P, Q)，P 与 Q 是整数且满足 0<=P<Q<N 。
如果满足以下条件，则称子数组(P, Q)为等差数组：
元素 A[P], A[p + 1], ..., A[Q - 1], A[Q] 是等差的。并且P + 1 < Q 。
函数要返回数组 A 中所有为等差数组的子数组个数。
示例:
A = [1, 2, 3, 4]
返回: 3, A 中有三个子等差数组: [1, 2, 3], [2, 3, 4] 以及自身 [1, 2, 3, 4]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/arithmetic-slices
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    # 方法一，数学法，44ms,41.11%
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        n = len(A)
        if n < 3:
            return 0
        ans = [0] * n
        con = [0] * n
        for i in range(2, n):
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                con[i] = con[i - 1] + 1 if con[i - 1] > 0 else 3
                ans[i] = ans[i - 1] + con[i] - 2
        result = 0
        for idx, num in enumerate(ans):
            if idx > 0 and num < ans[idx - 1]:
                result += ans[idx - 1]
        return result + ans[-1]

    # 方法二，动态规划，40ms,64%
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        if len(A) < 3:
            return 0
        dp = dict()
        dp[0] = 0
        dp[1] = 0
        for i in range(2, len(A)):
            if A[i] + A[i - 2] == A[i - 1] * 2:
                dp[i] = 1 + dp[i - 1]
            else:
                dp[i] = 0
        return sum(dp.values())


if __name__ == '__main__':
    s = Solution()
    print(s.numberOfArithmeticSlices(A=[1, 2, 3]))
    print(s.numberOfArithmeticSlices(A=[1, 2, 3, 4]))
    print(s.numberOfArithmeticSlices(A=[1, 2, 3, 4, 5]))
    print(s.numberOfArithmeticSlices(A=[1, 2, 3, 4, 5, 6, 7]))
    print(s.numberOfArithmeticSlices(A=[1, 2, 3, 4, 5, 0, 0]))
    print(s.numberOfArithmeticSlices(A=[1, 2, 3, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0]))
    # 空数组
    print(s.numberOfArithmeticSlices([]))
