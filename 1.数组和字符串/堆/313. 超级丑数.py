"""
超级丑数 是一个正整数，并满足其所有质因数都出现在质数数组 primes 中。

给你一个整数 n 和一个整数数组 primes ，返回第 n 个 超级丑数 。

题目数据保证第 n 个 超级丑数 在 32-bit 带符号整数范围内。



示例 1：

输入：n = 12, primes = [2,7,13,19]
输出：32 
解释：给定长度为 4 的质数数组 primes = [2,7,13,19]，前 12 个超级丑数序列为：[1,2,4,7,8,13,14,16,19,26,28,32] 。
示例 2：

输入：n = 1, primes = [2,3,5]
输出：1
解释：1 不含质因数，因此它的所有质因数都在质数数组 primes = [2,3,5] 中。

提示：

1 <= n <= 106
1 <= primes.length <= 100
2 <= primes[i] <= 1000
题目数据 保证 primes[i] 是一个质数
primes 中的所有值都 互不相同 ，且按 递增顺序 排列

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/super-ugly-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import heapq
from typing import List


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        # import heapq
        arr = [1]
        visited = {1}
        while n > 0:
            ugly = heapq.heappop(arr)
            for pri in primes:
                temp = ugly * pri
                if temp not in visited:
                    visited.add(temp)
                    heapq.heappush(arr, temp)
            n -= 1
        return ugly


class Solution:
    """
    前言
    这道题和「264. 丑数 II」相似，区别在于，第 264 题规定丑数是只包含质因数 2、3 和 5 的正整数，
    这道题规定超级丑数是只包含数组 primes 中的质因数的正整数。
    这道题可以使用第 264 题的方法，包括最小堆和动态规划。

    方法一：最小堆
    要得到从小到大的第 n 个超级丑数，可以使用最小堆实现。
    初始时堆为空。首先将最小的超级丑数 1 加入堆。
    每次取出堆顶元素 x，则 x 是堆中最小的超级丑数。对于数组 primes 的任意质数 p，px 也是超级丑数，
    因此将数组 primes 中的每个质数和 x 的乘积分别加入堆。

    上述做法会导致堆中出现重复元素的情况。为了避免重复元素，可以使用哈希集合去重，避免相同元素多次加入堆。
    在排除重复元素的情况下，第 n 次从最小堆中取出的元素即为第 n 个超级丑数。

    作者：LeetCode-Solution
    链接：https://leetcode-cn.com/problems/super-ugly-number/solution/chao-ji-chou-shu-by-leetcode-solution-uzff/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        seen = {1}
        heap = [1]

        for i in range(n):
            ugly = heapq.heappop(heap)
            for prime in primes:
                nxt = ugly * prime
                if nxt not in seen:
                    seen.add(nxt)
                    heapq.heappush(heap, nxt)

        return ugly
