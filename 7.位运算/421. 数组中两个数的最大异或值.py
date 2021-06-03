"""
给你一个整数数组 nums ，返回 nums[i] XOR nums[j] 的最大运算结果，其中 0 ≤ i ≤ j < n 。

进阶：你可以在 O(n) 的时间解决这个问题吗？



示例 1：

输入：nums = [3,10,5,25,2,8]
输出：28
解释：最大运算结果是 5 XOR 25 = 28.
示例 2：

输入：nums = [0]
输出：0
示例 3：

输入：nums = [2,4]
输出：6
示例 4：

输入：nums = [8,10,2]
输出：10
示例 5：

输入：nums = [14,70,53,83,49,91,36,80,92,51,66,70]
输出：127


提示：

1 <= nums.length <= 2 * 104
0 <= nums[i] <= 231 - 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-xor-of-two-numbers-in-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    """
    假设我们在数组中选择了元素 a_i和 a_j（i!=j），使得它们达到最大的按位异或运算结果 x：
    x = a_i ⊕ a_j
    其中 ⊕ 表示按位异或运算。要想求出 x，一种简单的方法是使用二重循环枚举 i 和 j，但这样做的时间复杂度为 O(n^2)，
    会超出时间限制。因此，我们需要寻求时间复杂度更低的做法。

    根据按位异或运算的性质，x = a_i ⊕ a_j，等价于 a_j = x ⊕ a_ia。
    我们可以根据这一变换，设计一种「从高位到低位依次确定 x 二进制表示的每一位」的方法，以此得到 x 的值。
    该方法的精髓在于：
    1·由于数组中的元素都在 [0, 2^31)的范围内，那么我们可以将每一个数表示为一个长度为31 位的二进制数（
    如果不满 31 位，在最高位之前补上若干个前导 0 即可）；

    2·这 31 个二进制位从低位到高位依次编号为 0,1,⋯,30。
    我们从最高位第 30 个二进制位开始，依次确定 x 的每一位是 0 还是 1；

    3·由于我们需要找出最大的 x，因此在枚举每一位时，我们先判断 x 的这一位是否能取到 1。
    如果能，我们取这一位为 1，否则我们取这一位为 0。

    「判断 xx 的某一位是否能取到 1」这一步骤并不容易。下面介绍两种判断的方法。

    方法一：哈希表
    思路与算法

    假设我们已经确定了 x 最高的若干个二进制位，当前正在确定第 k 个二进制位。
    根据「前言」部分的分析，我们希望第 k 个二进制位能够取到 1。

    我们用 \textit{pre}^k(x)pre
    k
     (x) 表示 xx 从最高位第 30 个二进制位开始，到第 k 个二进制位为止的数，那么 a_j = x \oplus a_ia
    j

     =x⊕a
    i

      蕴含着：

    \textit{pre}^k (a_j) = \textit{pre}^k (x) \oplus \textit{pre}^k (a_i)
    pre
    k
     (a
    j

     )=pre
    k
     (x)⊕pre
    k
     (a
    i

     )

    由于 \textit{pre}^k(x)pre
    k
     (x) 对于我们来说是已知的，因此我们将所有的 \textit{pre}^k (a_j)pre
    k
     (a
    j

     ) 放入哈希表中，随后枚举 ii 并计算 \textit{pre}^k (x) \oplus \textit{pre}^k (a_i)pre
    k
     (x)⊕pre
    k
     (a
    i

     )。如果其出现在哈希表中，那么说明第 kk 个二进制位能够取到 11，否则第 kk 个二进制位只能为 00。

    本方法若仅阅读文字，理解起来可能较为困难，读者可以参考下面的代码以及注释。

    细节

    计算 \textit{pre}^k(x)pre
    k
     (x) 可以使用右移运算 \texttt{>>}>>。

    作者：LeetCode-Solution
    链接：https://leetcode-cn.com/problems/maximum-xor-of-two-numbers-in-an-array/solution/shu-zu-zhong-liang-ge-shu-de-zui-da-yi-h-n9m9/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def findMaximumXOR(self, nums: List[int]) -> int:
        # 最高位的二进制位编号为 30
        HIGH_BIT = 30

        x = 0
        for k in range(HIGH_BIT, -1, -1):
            seen = set()
            # 将所有的 pre^k(a_j) 放入哈希表中
            for num in nums:
                # 如果只想保留从最高位开始到第 k 个二进制位为止的部分
                # 只需将其右移 k 位
                seen.add(num >> k)

            # 目前 x 包含从最高位开始到第 k+1 个二进制位为止的部分
            # 我们将 x 的第 k 个二进制位置为 1，即为 x = x*2+1
            x_next = x * 2 + 1
            found = False

            # 枚举 i
            for num in nums:
                if x_next ^ (num >> k) in seen:
                    found = True
                    break

            if found:
                x = x_next
            else:
                # 如果没有找到满足等式的 a_i 和 a_j，那么 x 的第 k 个二进制位只能为 0
                # 即为 x = x*2
                x = x_next - 1

        return x


if __name__ == '__main__':
    s = Solution()
    print(s.findMaximumXOR(nums=[3, 10, 5, 25, 2, 8]))
