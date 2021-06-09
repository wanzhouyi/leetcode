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


if __name__ == '__main__':
    s = Solution()
    print(s.findTargetSumWays(nums=[1, 1, 1, 1, 1], target=3))  # 5
    print(s.findTargetSumWays(nums=[1], target=1))  # 1
    print(s.findTargetSumWays(
        [6, 44, 30, 25, 8, 26, 34, 22, 10, 18, 34, 8, 0, 32, 13, 48, 29, 41, 16, 30], 12))
    print(s.findTargetSumWays(
        [10, 34, 28, 5, 10, 26, 9, 17, 28, 10, 9, 6, 10, 15, 0, 28, 42, 39, 25, 19], 26))
    print(s.findTargetSumWays(
        [42, 1, 42, 35, 33, 37, 26, 3, 23, 29, 22, 50, 34, 31, 11, 28, 20, 31, 32, 28], 2))
    print(s.findTargetSumWays(
        [11, 31, 37, 36, 43, 40, 50, 18, 10, 15, 10, 35, 43, 25, 41, 43, 6, 22, 38, 38], 44))
