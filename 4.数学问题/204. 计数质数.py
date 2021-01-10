"""
统计所有小于非负整数n的质数的数量。

示例 1：
输入：n = 10
输出：4
解释：小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。

示例 2：
输入：n = 0
输出：0

示例 3：
输入：n = 1
输出：0

提示：

0 <= n <= 5 * 106

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-primes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def countPrimes(self, n: int) -> int:
        """
        枚举没有考虑到数与数的关联性，因此难以再继续优化时间复杂度。
        接下来我们介绍一个常见的算法，该算法由希腊数学家厄拉多塞提出，称为厄拉多塞筛法，简称埃氏筛。
        我们考虑这样一个事实：如果 x 是质数，那么大于 x 的 x 的倍数 2x,3x,… 一定不是质数，因此我们可以从这里入手。
        我们设isPrime[i] 表示数 i 是不是质数，如果是质数则为 1，否则为 0。从小到大遍历每个数，
        如果这个数为质数，则将其所有的倍数都标记为合数（除了该质数本身），即0，这样在运行结束的时候我们即能知道质数的个数。
        """
        is_prime = [True] * n  # 初始化全为素数
        for i in range(2, n):
            if is_prime[i]:  # 如果 i 是素数，则 i 的倍数不可能是素数，置为 False
                j = i * 2
                while j < n:
                    is_prime[j] = False
                    j += i
        count = 0
        for i in range(2, n):
            if is_prime[i]:
                count += 1

        return count


if __name__ == '__main__':
    s = Solution()
    print(s.countPrimes(10))
