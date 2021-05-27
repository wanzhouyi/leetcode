"""
两个整数的汉明距离 指的是这两个数字的二进制数对应位不同的数量。

计算一个数组中，任意两个数之间汉明距离的总和。

示例:

输入: 4, 14, 2

输出: 6

解释: 在二进制表示中，4表示为0100，14表示为1110，2表示为0010。（这样表示是为了体现后四位之间关系）
所以答案为：
HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.
注意:

数组中元素的范围为从0到10^9。
数组的长度不超过10^4。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/total-hamming-distance
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        # 暴力会超时
        # bit_nums = list(map(lambda x: x & 0xffffffff, nums))
        ans = 0
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                ans += bin(nums[i] ^ nums[j] & 0xffffffff).count('1')
        return ans


class Solution:
    """
    在计算汉明距离时，我们考虑的是同一比特位上的值是否不同，而不同比特位之间是互不影响的。

    对于数组 nums 中的某个元素 val，若其二进制的第 i 位为 1，我们只需统计nums 中有多少元素的第 i 位为 0，即计算出了val 与其他元素在第 i 位上的汉明距离之和。

    具体地，若长度为 n 的数组 nums 的所有元素二进制的第 i 位共有 c 个 1，n−c 个 0，则些元素在二进制的第 i 位上的汉明距离之和为

    c⋅(n−c)

    我们可以从二进制的最低位到最高位，逐位统计汉明距离。将每一位上得到的汉明距离累加即为答案。

    具体实现时，对于整数 val 二进制的第 i 位，我们可以用代码 (val >> i) & 1 来取出其第 i 位的值。此外，由于 10^9<2^30
     ，我们可以直接从二进制的第 0 位枚举到第 29 位。

    作者：LeetCode-Solution
    链接：https://leetcode-cn.com/problems/total-hamming-distance/solution/yi-ming-ju-chi-zong-he-by-leetcode-solut-t0ev/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def totalHammingDistance(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(30):
            c = sum(((val >> i) & 1) for val in nums)
            ans += c * (n - c)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.totalHammingDistance([4, 14, 2]))
