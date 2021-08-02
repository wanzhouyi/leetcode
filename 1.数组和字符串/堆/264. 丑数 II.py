"""
给你一个整数 n ，请你找出并返回第 n 个 丑数 。
丑数 就是只包含质因数2、3 和/或5的正整数。

示例 1：
输入：n = 10
输出：12
解释：[1, 2, 3, 4, 5, 6, 8, 9, 10, 12] 是由前 10 个丑数组成的序列。
示例 2：
输入：n = 1
输出：1
解释：1 通常被视为丑数。

提示：

1 <= n <= 1690

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ugly-number-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import heapq


class Solution:
    """
    方法一：最小堆
    要得到从小到大的第 nn 个丑数，可以使用最小堆实现。
    初始时堆为空。首先将最小的丑数 1 加入堆。
    每次取出堆顶元素 x，则 xx 是堆中最小的丑数，由于 2x, 3x, 5x 也是丑数，因此将 2x, 3x, 5x加入堆。
    上述做法会导致堆中出现重复元素的情况。为了避免重复元素，可以使用哈希集合去重，避免相同元素多次加入堆。
    在排除重复元素的情况下，第 n 次从最小堆中取出的元素即为第 nn 个丑数。
    作者：LeetCode-Solution
    链接：https://leetcode-cn.com/problems/ugly-number-ii/solution/chou-shu-ii-by-leetcode-solution-uoqd/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def nthUglyNumber(self, n: int) -> int:
        factors = [2, 3, 5]
        seen = {1}
        heap = [1]

        for i in range(n - 1):
            curr = heapq.heappop(heap)
            for factor in factors:
                if (nxt := curr * factor) not in seen:
                    seen.add(nxt)
                    heapq.heappush(heap, nxt)

        return heapq.heappop(heap)


class Solution(object):
    """
    解题思路
今天的题目让我们生成第 n 个丑数。做这样的题目，如果是逐个判断自然数是否为丑数，一定是会超时的。常见的办法是用生成的办法。

要生成第 n 个丑数，我们必须从第一个丑数 1 开始，向后逐渐的寻找。丑数只包含 2， 3，5 三个因子，所以生成方式就是在已经生成的丑数集合中乘以 [2, 3, 5] 而得到新的丑数。

现在的问题是在已经生成的丑数集合中，用哪个数字乘以 2？ 用哪个数字乘以 3？用哪个数字乘以 5？

很显然的一个结论：用还没乘过 2 的最小丑数乘以 2；用还没乘过 3 的最小丑数乘以 3；用还没乘过 5 的最小丑数乘以 5。然后在得到的数字中取最小，就是新的丑数。

实现的方法是用动态规划：

我们需要定义 3 个指针 index2, index3, index5 分别表示丑数集合中还没乘过 2，3，5 的丑数位置。
然后每次新的丑数 dp[i] = min(dp[index2] * 2, dp[index3] * 3, dp[index5] * 5) 。
然后根据 dp[i] 是由 index2, index3, index5 中的哪个相乘得到的，对应的把此 index + 1，表示还没乘过该 index 的最小丑数变大了。

作者：fuxuemingzhu
链接：https://leetcode-cn.com/problems/ugly-number-ii/solution/fu-xue-ming-zhu-gai-shui-cheng-yi-2-3-5-92zlw/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def nthUglyNumber(self, n):
        if n < 0:
            return 0
        dp = [1] * n
        index2, index3, index5 = 0, 0, 0
        for i in range(1, n):
            dp[i] = min(2 * dp[index2], 3 * dp[index3], 5 * dp[index5])
            if dp[i] == 2 * dp[index2]: index2 += 1
            if dp[i] == 3 * dp[index3]: index3 += 1
            if dp[i] == 5 * dp[index5]: index5 += 1
        return dp[n - 1]


if __name__ == '__main__':
    s = Solution()
    print(s.nthUglyNumber(n=10))
    # print(s.nthUglyNumber(n=1))
    # print(s.nthUglyNumber(n=1500))
