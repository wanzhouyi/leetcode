"""
实现pow(x, n)，即计算 x 的 n 次幂函数（即，xn）。

示例 1：
输入：x = 2.00000, n = 10
输出：1024.00000

示例 2：
输入：x = 2.10000, n = 3
输出：9.26100

示例 3：
输入：x = 2.00000, n = -2
输出：0.25000
解释：2-2 = 1/22 = 1/4 = 0.25

提示：
-100.0 <x< 100.0
-231<= n <=231-1
-104 <= xn <= 104

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/powx-n
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x ** n


class Solution:
    def myPow(self, x: float, n: int) -> float:
        # self.cnt=0
        ans = self.merge_pow(x, abs(n))
        if n < 0:
            ans = 1 / ans
        # print(self.cnt)
        return ans

    def merge_pow(self, x: float, n: int):
        # self.cnt += 1
        if n == 0:
            return 1
        elif n == 1:
            return x
        mid = n // 2
        left = self.merge_pow(x, mid)
        if n % 2 == 0:
            return left * left
        else:
            return left * left * x


class Solution:
    """
    方法一：快速幂 + 递归
「快速幂算法」的本质是分治算法。举个例子，如果我们要计算 x^64 ，我们可以按照：
x--> x^2 --> x^4 --> x^8 --> x^16 --> x^32 --> x^64
的顺序，从 x 开始，每次直接把上一次的结果进行平方，计算 6 次就可以得到 x^64的值，而不需要对 x 乘 63 次 x。

再举一个例子，如果我们要计算 x^77，我们可以按照：

x --> x^2 --> x^4 --> x^9 --> x^19 --> x^38 --> x^77的顺序，
在 x --> x^2，x^2 --> x^4，x^19 --> x^38 这些步骤中，我们直接把上一次的结果进行平方，
而在 x^4 --> x^9，x^9 --> x^19，x^38 --> x^77这些步骤中，我们把上一次的结果进行平方后，还要额外乘一个 x。
直接从左到右进行推导看上去很困难，因为在每一步中，我们不知道在将上一次的结果平方之后，还需不需要额外乘 x。但如果我们从右往左看，分治的思想就十分明显了：

当我们要计算 x^n时，我们可以先递归地计算出 y = x^{n/2}
 ，其中 ⌊a⌋ 表示对 a 进行下取整；

根据递归计算的结果，如果 n 为偶数，那么 x^n = y^2；如果 n 为奇数，那么 x^n = y^2*x
递归的边界为 n = 0，任意数的 0 次方均为 1。

由于每次递归都会使得指数减少一半，因此递归的层数为 O(logn)，算法可以在很快的时间内得到结果。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/powx-n/solution/powx-n-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def myPow(self, x: float, n: int) -> float:
        def quickMul(N):
            if N == 0:
                return 1.0
            y = quickMul(N // 2)
            return y * y if N % 2 == 0 else y * y * x

        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)


if __name__ == '__main__':
    s = Solution()
    print(s.myPow(x=2.00000, n=10))
    print(s.myPow(0.00001, 2147483647))
