"""
给你一个整数数组 nums 和一个整数 target 。
向数组中的每个整数前添加'+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ：
例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。

示例 1：
输入：nums = [1,1,1,1,1], target = 3
输出：5
解释：一共有 5 种方法让最终目标和为 3 。
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
示例 2：

输入：nums = [1], target = 1
输出：1

提示：

1 <= nums.length <= 20
0 <= nums[i] <= 1000
0 <= sum(nums[i]) <= 1000
-1000 <= target <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/target-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List

from functools import lru_cache


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        max_idx = len(nums) - 1
        counter = 0

        @lru_cache(None)
        def dfs(idx, sm):
            nonlocal counter
            counter += 1
            if idx == max_idx:
                temp_ans = 0
                if sm + nums[idx] == target:
                    temp_ans += 1
                if sm - nums[idx] == target:
                    temp_ans += 1
                return temp_ans

            add = dfs(idx + 1, sm + nums[idx])
            sub = dfs(idx + 1, sm - nums[idx])
            return add + sub

        ans = dfs(0, 0)
        print(counter)
        return ans

class Solution:
    """
    01背包
    思路
    原问题是给定一些数字，加加减减，使得它们等于targert。例如，1 - 2 + 3 - 4 + 5 = target(3)。
    如果我们把加的和减的结合在一起，可以写成
    (1+3+5)  +  (-2-4) = target(3)
    -------     ------
     -> 正数    -> 负数
    所以，我们可以将原问题转化为： 找到nums一个正子集和一个负子集，使得总和等于target，统计这种可能性的总数。
    我们假设P是正子集，N是负子集。让我们看看如何将其转换为子集求和问题：

                      sum(P) - sum(N) = target
                      （两边同时加上sum(P)+sum(N)）
    sum(P) + sum(N) + sum(P) - sum(N) = target + sum(P) + sum(N)
                (因为 sum(P) + sum(N) = sum(nums))
                           2 * sum(P) = target + sum(nums)
    因此，原来的问题已转化为一个求子集的和问题： 找到nums的一个子集 P，使得

    sum(P) = (target + sum(nums))//2
    根据公式，若target + sum(nums)不是偶数，就不存在答案，即返回0个可能解。

    因此题目转化为01背包，也就是能组合成容量为sum(P)的方式有多少种,一种组合中每个数字只能取一次
    解决01背包问题使用的是动态规划的思想。

    方法是

    开辟一个长度为P+1的数组，命名为dp
    dp的第x项，代表组合成数字x有多少方法。比如说,dp[0] = 1，代表组合成0只有1中方法，即什么也不取。
    比如说dp[5] = 3 ，代表使总和加到5总共有三种方法。
    所以最后返回的就是dp[P]，代表组合成P的方法有多少种
    ------------------------------
    问题是
    怎么更新dp数组呢？

    遍历nums，遍历的数记作num
    再逆序遍历从P到num，遍历的数记作j
    更新dp[j] = dp[j - num] + dp[j]
    这样遍历的含义是，对每一个在nums数组中的数num而言，dp在从num到P的这些区间里，都可以加上一个num，来到达想要达成的P。
    举例来说，对于数组[1,2,3,4,5]，想要康康几种方法能组合成4,那么设置dp[0]到dp[4]的数组
    假如选择了数字2,那么dp[2:5]（也就是2到4）都可以通过加上数字2有所改变，
    而dp[0:2]（也就是0到1）加上这个2很明显就超了，就不管它。
    以前没有考虑过数字2,考虑了会怎么样呢？就要更新dp[2:5]，比如说当我们在更新dp[3]的时候，
    就相当于dp[3] = dp[3] + dp[1],即本来有多少种方法，加上去掉了2以后有多少种方法。
    因为以前没有考虑过2,现在知道，只要整到了1,就一定可以整到3。
    为什么以这个顺序来遍历呢？
    假如给定nums = [num1,num2,num3]，我们现在可以理解dp[j] = dp[j-num1] + dp[j-num2] + dp[j-num3]。

    但是如何避免不会重复计算或者少算？要知道，我们的nums并不是排序的，我们的遍历也不是从小到大的。

    我们不妨跟着流程走一遍

    第一次num1，仅仅更新了dp[num1] = 1，其他都是0+0都是0啊都是0
    第二次num2，更新了dp[num2] = 1和dp[num1+num2] = dp[num1+num2] + dp[num1] = 1,先更新后者。
    第三次num3，更新了dp[num3] = 1和dp[num1+num3] += 1和dp[num2+num3] += 1和dp[num1+num2+num3] += 1。按下标从大到小顺序来更新。
    ......
    由此可见，这种顺序遍历能得到最后的答案。这里可以跟着IDE的debug功能走一遍，加深理解。

    作者：qsctech-sange
    链接：https://leetcode-cn.com/problems/target-sum/solution/python-dfs-xiang-jie-by-jimmy00745/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if sum(nums) < target or (sum(nums) + target) % 2 == 1: return 0
        P = (sum(nums) + target) // 2
        dp = [1] + [0 for _ in range(P)]
        for num in nums:
            for j in range(P, num - 1, -1):
                dp[j] += dp[j - num]
        return dp[P]
if __name__ == '__main__':
    s = Solution()
    print(s.findTargetSumWays(nums=[1, 1, 1, 1, 1], target=3))  # 5
    # print(s.findTargetSumWays(nums=[1], target=1))  # 1
    # print(s.findTargetSumWays(
    #     [6, 44, 30, 25, 8, 26, 34, 22, 10, 18, 34, 8, 0, 32, 13, 48, 29, 41, 16, 30], 12))
    # print(s.findTargetSumWays(
    #     [10, 34, 28, 5, 10, 26, 9, 17, 28, 10, 9, 6, 10, 15, 0, 28, 42, 39, 25, 19], 26))
    # print(s.findTargetSumWays(
    #     [42, 1, 42, 35, 33, 37, 26, 3, 23, 29, 22, 50, 34, 31, 11, 28, 20, 31, 32, 28], 2))
    # print(s.findTargetSumWays(
    #     [11, 31, 37, 36, 43, 40, 50, 18, 10, 15, 10, 35, 43, 25, 41, 43, 6, 22, 38, 38], 44))
