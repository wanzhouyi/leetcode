"""
给定一个整数数组 A，返回其中元素之和可被 K整除的（连续、非空）子数组的数目。

示例：
输入：A = [4,5,0,-2,-3,1], K = 5
输出：7
解释：
有 7 个子数组满足其元素之和可被 K = 5 整除：
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]

提示：

1 <= A.length <= 30000
-10000 <= A[i] <= 10000
2 <= K <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subarray-sums-divisible-by-k
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    """
    方法一：哈希表 + 逐一统计
    思路和算法
    通常，涉及连续子数组问题的时候，我们使用前缀和来解决。
    我们令P[i]=nums[0]+nums[1]+…+nums[i]。那么每个连续子数组的和sum(i,j) 就可以写成P[j]−P[i−1]（其中 0 < i < j）的形式。
    此时，判断子数组的和能否被 k 整除就等价于判断(P[j]−P[i−1])% k ==0，
    根据 同余定理，只要P[j]%k==P[i−1]%k，就可以保证上面的等式成立。

    因此我们可以考虑对数组进行遍历，在遍历同时统计答案。当我们遍历到第 i 个元素时，我们统计以 i 结尾的符合条件的子数组个数。
    我们可以维护一个以前缀和模 k 的值为键，出现次数为值的哈希表record，在遍历的同时进行更新。
    这样在计算以 i 结尾的符合条件的子数组个数时，根据上面的分析，答案即为 [0..i-1]中前缀和模 k 也为 P[i]%k 的位置个数，
    即record[P[i]%k]。

    最后的答案即为以每一个位置为数尾的符合条件的子数组个数之和。
    需要注意的一个边界条件是，我们需要对哈希表初始化，记录record[0]=1，这样就考虑了前缀和本身被 k 整除的情况。

    注意：不同的语言负数取模的值不一定相同，有的语言为负数，对于这种情况需要特殊处理。

    作者：LeetCode-Solution
    链接：https://leetcode-cn.com/problems/subarray-sums-divisible-by-k/solution/he-ke-bei-k-zheng-chu-de-zi-shu-zu-by-leetcode-sol/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        record = {0: 1}
        total, ans = 0, 0
        for elem in nums:
            total += elem
            modulus = total % k
            same = record.get(modulus, 0)
            ans += same
            record[modulus] = same + 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.subarraysDivByK(nums=[4, 5, 0, -2, -3, 1], k=5))
