"""
给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。
例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。

示例 1：
输入：nums = [10,9,2,5,3,7,101,18]
输出：4
解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。

示例 2：
输入：nums = [0,1,0,3,2,3]
输出：4

示例 3：
输入：nums = [7,7,7,7,7,7,7]
输出：1

提示：

1 <= nums.length <= 2500
-104 <= nums[i] <= 104


进阶：

你可以设计时间复杂度为 O(n2) 的解决方案吗？
你能将算法的时间复杂度降低到O(n log(n)) 吗?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-increasing-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    # 动态规划
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        动态规划
        思路与算法

        定义dp[i] 为考虑前 i 个元素，以第 i 个数字结尾的最长上升子序列的长度，注意nums[i] 必须被选取。
        我们从小到大计算 dp[] 数组的值，在计算 dp[i]之前，我们已经计算出 dp[0…i−1] 的值，则状态转移方程为：
        dp[i]=max(dp[j])+1,其中0≤j<i且num[j]<num[i]

        即考虑往dp[0…i−1] 中最长的上升子序列后面再加一个nums[i]。由于dp[j] 代表nums[0…j] 中以 nums[j] 结尾的最长上升子序列，
        所以如果能从 dp[j]这个状态转移过来，那么nums[i] 必然要大于nums[j]，才能将nums[i] 放在nums[j] 后面以形成更长的上升子序列。

        最后，整个数组的最长上升子序列即所有 dp[i]中的最大值。
        LIS_length=max(dp[i]),其中0≤i<n
        """
        if not nums:
            return 0
        n = len(nums)
        ls = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    ls[i] = max(ls[j] + 1, ls[i])
        return max(ls)

    # 贪心 + 二分查找
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        贪心 + 二分查找
        考虑一个简单的贪心，如果我们要使上升子序列尽可能的长，则我们需要让序列上升得尽可能慢，因此我们希望每次在上升子序列最后加上的那个数尽可能的小。
        基于上面的贪心思路，我们维护一个数组d[i] ，表示长度为 ii 的最长上升子序列的末尾元素的最小值，用len 记录目前最长上升子序列的长度，起始时 len 为 1，d[1]=nums[0]。
        我们依次遍历数组 nums[] 中的每个元素，并更新数组 d[] 和 len 的值。
        如果nums[i]>d[len] 则更新 len = len + 1，
        否则在 d[1…len]中找满足 d[i−1]<nums[j]<d[i] 的下标 i，并更新 d[i]=nums[j]。

        根据 dd 数组的单调性，我们可以使用二分查找寻找下标 i，优化时间复杂度。

        最后整个算法流程为：

        设当前已求出的最长上升子序列的长度为 len（初始时为 1），从前往后遍历数组 nums，在遍历到 nums[i] 时：

        如果 nums[i]>d[len] ，则直接加入到 d 数组末尾，并更新len=len+1；

        否则，在 d数组中二分查找，找到第一个比 nums[i] 小的数 d[k] ，并更新d[k+1]=nums[i]。
        以输入序列 [0, 8, 4, 12, 2] 为例：
        第一步插入 0，d = [0]；
        第二步插入 8，d = [0, 8]；
        第三步插入 4，d = [0, 4]；
        第四步插入 12，d = [0, 4, 12]；
        第五步插入 2，d = [0, 2, 12]。
        最终得到最大递增子序列长度为 3。

        作者：LeetCode-Solution
        链接：https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/zui-chang-shang-sheng-zi-xu-lie-by-leetcode-soluti/
        来源：力扣（LeetCode）
        著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        """
        d = []
        for num in nums:
            if not d or num > d[-1]:
                d.append(num)
            else:
                left, right = 0, len(d) - 1
                loc = right
                while left <= right:
                    mid = (left + right) // 2
                    if d[mid] >= num:
                        loc = mid
                        right = mid - 1
                    else:
                        left = mid + 1
                d[loc] = num
        return len(d)


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLIS(nums=[10, 9, 2, 5, 3, 7, 101, 18]))
    print(s.lengthOfLIS([]))
