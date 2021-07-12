"""
给你一个 只包含正整数 的 非空 数组nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。



示例 1：

输入：nums = [1,5,11,5]
输出：true
解释：数组可以分割成 [1, 5, 5] 和 [11] 。
示例 2：

输入：nums = [1,2,3,5]
输出：false
解释：数组不能分割成两个元素和相等的子集。


提示：

1 <= nums.length <= 200
1 <= nums[i] <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/partition-equal-subset-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from functools import lru_cache
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sm = sum(nums)
        if sm % 2 != 0:
            return False

        half_sum = sm // 2
        n = len(nums)

        @lru_cache(None)
        def dp(index, current_sum):
            if index == n:
                return False

            if current_sum == half_sum:
                return True

            if current_sum > half_sum:
                return False

            # 选
            if dp(index + 1, current_sum + nums[index]):
                return True

            # 不选
            if dp(index + 1, current_sum):
                return True

            return False

        return dp(0, 0)


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        sm = sum(nums)
        if sm % 2 != 0:
            return False
        half_sum = sm // 2

        dp = [[False] * (half_sum + 1) for _ in range(n)]
        dp[0][0] = True
        for i in range(n):
            for j in range(half_sum + 1):
                if nums[i] == j:
                    dp[i][j] = True
                elif dp[i - 1][j] == True:
                    dp[i][j] = True
                elif j >= nums[i] and dp[i - 1][j - nums[i]] == True:
                    dp[i][j] = True

        return dp[-1][-1]


class Solution:
    """
    方法一：动态规划
    思路与算法

    这道题可以换一种表述：给定一个只包含正整数的非空数组 nums[0]，判断是否可以从数组中选出一些数字，
    使得这些数字的和等于整个数组的元素和的一半。因此这个问题可以转换成「0−1 背包问题」。
    这道题与传统的「0-1背包问题」的区别在于，传统的「0−1 背包问题」要求选取的物品的重量之和不能超过背包的总容量，
    这道题则要求选取的数字的和恰好等于整个数组的元素和的一半。类似于传统的「0−1 背包问题」，可以使用动态规划求解。

    在使用动态规划求解之前，首先需要进行以下判断。

    根据数组的长度 n 判断数组是否可以被划分。如果 n<2，则不可能将数组分割成元素和相等的两个子集，因此直接返回false。
    计算整个数组的元素和 sum 以及最大元素maxNum。如果sum 是奇数，则不可能将数组分割成元素和相等的两个子集，因此直接返回false。
    如果sum 是偶数，则令target= sum/2，需要判断是否可以从数组中选出一些数字，使得这些数字的和等于 target。
    如果 maxNum>target，则除了maxNum 以外的所有元素之和一定小于target，因此不可能将数组分割成元素和相等的两个子集，直接返回false。

    创建二维数组 dp，包含 n行target+1 列，其中dp[i][j] 表示从数组的[0,i] 下标范围内选取若干个正整数（可以是 0 个），
    是否存在一种选取方案使得被选取的正整数的和等于 j。初始时，\dp 中的全部元素都是false。

    在定义状态之后，需要考虑边界情况。以下两种情况都属于边界情况。
    如果不选取任何正整数，则被选取的正整数等于 0。因此对于所有0≤i<n，都有 dp[i][0]=true。
    当 i==0时，只有一个正整数 nums[0] 可以被选取，因此 dp[0][nums[0]]=true。

    对于 i>0 且 j>0 的情况，如何确定 dp[i][j] 的值？需要分别考虑以下两种情况。

    如果 j≥nums[i]，则对于当前的数字 nums[i]，可以选取也可以不选取，两种情况只要有一个为true，就有 dp[i][j]=true。
    如果不选取 nums[i]，则 dp[i][j]=dp[i−1][j]；
    如果选取 nums[i]，则dp[i][j]=dp[i−1][j−nums[i]]。
    如果 j<nums[i]，则在选取的数字的和等于 j 的情况下无法选取当前的数字nums[i]，因此有 dp[i][j]=dp[i−1][j]。
    状态转移方程如下：

    dp[i][j]={
    dp[i−1][j] or dp[i−1][j−nums[i]],  j≥nums[i]
    dp[i−1][j],  j<nums[i]
    }

    最终得到dp[n−1][target] 即为答案。

    作者：LeetCode-Solution
    链接：https://leetcode-cn.com/problems/partition-equal-subset-sum/solution/fen-ge-deng-he-zi-ji-by-leetcode-solution/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2:
            return False

        total = sum(nums)
        maxNum = max(nums)
        if total & 1:
            return False

        target = total // 2
        if maxNum > target:
            return False

        dp = [[0] * (target + 1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = True

        dp[0][nums[0]] = True
        for i in range(1, n):
            num = nums[i]
            for j in range(1, target + 1):
                if j >= num:
                    dp[i][j] = dp[i - 1][j] | dp[i - 1][j - num]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[n - 1][target]
