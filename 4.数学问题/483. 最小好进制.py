"""
对于给定的整数 n, 如果n的k（k>=2）进制数的所有数位全为1，则称k（k>=2）是 n 的一个好进制。
以字符串的形式给出 n, 以字符串的形式返回 n 的最小好进制。

示例 1：

输入："13"
输出："3"
解释：13 的 3 进制是 111。
示例 2：

输入："4681"
输出："8"
解释：4681 的 8 进制是 11111。
示例 3：

输入："1000000000000000000"
输出："999999999999999999"
解释：1000000000000000000 的 999999999999999999 进制是 11。

提示：

n的取值范围是[3, 10^18]。
输入总是有效且没有前导 0。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/smallest-good-base
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import math


class Solution:
    """
    思路及解法
    假设正整数 n 在 k(k≥2) 进制下的所有数位都为 1，且位数为m+1，那么有：
    n = k^0 + k^1 + k^2 + …… + k^m
    我们首先讨论两种特殊情况：

    m=0，此时 n=1，而题目保证n≥3，所以本题中 m>0。
    m=1，此时 n=(11)_k，即 k=n−1≥2，这保证了本题有解。

    作者：LeetCode-Solution
    链接：https://leetcode-cn.com/problems/smallest-good-base/solution/zui-xiao-hao-jin-zhi-by-leetcode-solutio-csqn/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def smallestGoodBase(self, n: str) -> str:
        max_p = int(math.log(int(n), 2))  # 如果用for循环对幂次p从1开始到n，肯定超时。这里能想到。
        for p in range(max_p, 0, -1):
            k = int(pow(int(n), 1.0 / p))  # 对k的范围确定，如果同样从1开始到n，肯定超时，这里想不到。
            # value = (pow(k,p+1)-1)/(k-1) # 如果用等比数列求和公式，肯定造成溢出，导致错误。

            ####  下面是计算等比数列求和
        sum_value = 1
        mul = 1
        for i in range(1, p + 1):  # 等比数列求和
            mul *= k
            sum_value += mul

        #  如果求和结果等于n，则直接返回str(k)
        if sum_value == int(n):
            return str(k)

        # 如果不满足上述要求，直接返回最大的k: 即 n-1
        return str(int(n) - 1)
