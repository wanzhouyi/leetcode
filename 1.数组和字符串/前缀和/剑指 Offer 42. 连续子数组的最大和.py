"""
输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。
要求时间复杂度为O(n)。
示例1:
输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释:连续子数组[4,-1,2,1] 的和最大，为6。
提示：

1 <=arr.length <= 10^5
-100 <= arr[i] <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 初始化前缀和数组
        pre_sum = [0]
        # until_min变量代表当前最小的前缀和。初始化为0不对后续计算产生影响。
        until_min = 0
        # 最终返回的结果，初始化为最大，滚动求值
        ans = float('-inf')
        for num in nums:
            # 当前数值为止的前缀和
            temp_sum = pre_sum[-1] + num
            # 滚动计算最大前缀和差值
            ans = max(ans, temp_sum - until_min)
            # 更新最小前缀和
            until_min = min(temp_sum, until_min)
            # 将当前前缀和添加到前缀和数组中
            pre_sum.append(temp_sum)
        return ans


class Solution:
    """
    动态规划解析：
    状态定义： 设动态规划列表 dp ，dp[i] 代表以元素 nums[i]为结尾的连续子数组最大和。
        为何定义最大和 dp[i] 中必须包含元素 nums[i] ：保证 dp[i] 递推到 dp[i+1] 的正确性；
        如果不包含 nums[i] ，递推时则不满足题目的 连续子数组 要求。
    转移方程： 若 dp[i−1]≤0 ，说明 dp[i - 1] 对 dp[i] 产生负贡献，即 dp[i-1] + nums[i]还不如 nums[i] 本身大。
        当 dp[i - 1] > 0时：执行 dp[i] = dp[i-1] + nums[i]；
        当 dp[i−1]≤0 时：执行 dp[i] = nums[i]；
    初始状态： dp[0] = nums[0]，即以 nums[0]结尾的连续子数组最大和为 nums[0] 。

    返回值： 返回 dp 列表中的最大值，代表全局最大值。

    空间复杂度降低：
    由于 dp[i]只与 dp[i-1] 和 nums[i] 有关系，因此可以将原数组 nums 用作 dp 列表，即直接在 nums上修改即可。
    由于省去 dp 列表使用的额外空间，因此空间复杂度从 O(N) 降至 O(1) 。
    复杂度分析：
    时间复杂度 O(N) ： 线性遍历数组 nums 即可获得结果，使用 O(N) 时间。
    空间复杂度 O(1) ： 使用常数大小的额外空间。

    作者：jyd
    链接：https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof/solution/mian-shi-ti-42-lian-xu-zi-shu-zu-de-zui-da-he-do-2/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += max(nums[i - 1], 0)
        return max(nums)


if __name__ == '__main__':
    s = Solution()
    print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(s.maxSubArray([-2]))
    print(s.maxSubArray([0]))
    print(s.maxSubArray([2]))
    print(s.maxSubArray([2, 5]))
    print(s.maxSubArray([-2, 5]))
    print(s.maxSubArray([2, -5]))
