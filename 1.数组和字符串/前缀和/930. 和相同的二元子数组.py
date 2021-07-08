"""
给你一个二元数组 nums ，和一个整数 goal ，请你统计并返回有多少个和为 goal 的 非空 子数组。
子数组 是数组的一段连续部分。

示例 1：
输入：nums = [1,0,1,0,1], goal = 2
输出：4
解释：
如下面黑体所示，有 4 个满足题目要求的子数组：
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]

示例 2：
输入：nums = [0,0,0,0,0], goal = 0
输出：15

提示：

1 <= nums.length <= 3 * 10^4
nums[i] 不是 0 就是 1
0 <= goal <= nums.length

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-subarrays-with-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        pre_sum = [0]
        ans = 0
        for num in nums:
            temp_sum = pre_sum[-1] + num
            ans += pre_sum.count(temp_sum - goal)
            pre_sum.append(temp_sum)

        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.numSubarraysWithSum(nums=[1, 0, 1, 0, 1], goal=2))
    print(s.numSubarraysWithSum(nums=[0, 0, 0, 0, 0], goal=0))
