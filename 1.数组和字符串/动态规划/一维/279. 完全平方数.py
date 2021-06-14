"""
给定正整数n，找到若干个完全平方数（比如1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

给你一个整数 n ，返回和为 n 的完全平方数的 最少数量 。

完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。



示例1：

输入：n = 12
输出：3 
解释：12 = 4 + 4 + 4
示例 2：

输入：n = 13
输出：2
解释：13 = 4 + 9

提示：

1 <= n <= 104

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/perfect-squares
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def numSquares(self, n: int) -> int:
        nums = [i * i for i in range(1, int(n ** 0.5) + 1)]
        f = [0] + [float('inf')] * n
        for num in nums:
            for j in range(num, n + 1):
                f[j] = min(f[j], f[j - num] + 1)
        return f[-1]


import math


class Solution:
    """
    方法一：动态规划
    思路及算法

    我们可以依据题目的要求写出状态表达式：f[i] 表示最少需要多少个数的平方来表示整数 i。

    这些数必然落在区间 [1,n的开方]。我们可以枚举这些数，假设当前枚举到 j，那么我们还需要取若干数的平方，构成 i-j^2。
    此时我们发现该子问题和原问题类似，只是规模变小了。这符合了动态规划的要求，于是我们可以写出状态转移方程。

    f[i]=1+\min_{j=1}^{\lfloor\sqrt{i}\rfloor}{f[i-j^2]}

    其中 f[0]=0 为边界条件，实际上我们无法表示数字 0，只是为了保证状态转移过程中遇到 j恰为 \sqrt{i}的情况合法。

    同时因为计算 f[i]时所需要用到的状态仅有 f[i-j^2]，必然小于 i，因此我们只需要从小到大地枚举 i 来计算f[i] 即可。

    作者：LeetCode-Solution
    链接：https://leetcode-cn.com/problems/perfect-squares/solution/wan-quan-ping-fang-shu-by-leetcode-solut-t99c/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def numSquares(self, n: int) -> int:
        f = [float('inf')] * (n + 1)
        f[0] = 0
        for i in range(1, n + 1):
            i_sqrt = math.sqrt(i)
            j = 1
            while j <= i_sqrt:
                f[i] = min(f[i], f[i - j * j] + 1)
                j += 1
        return f[n]


if __name__ == '__main__':
    s = Solution()
    print(s.numSquares(20))
    print(s.numSquares(956))
