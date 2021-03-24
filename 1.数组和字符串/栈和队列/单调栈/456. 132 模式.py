"""
给你一个整数数组 nums ，数组中共有 n 个整数。132 模式的子序列 由三个整数 nums[i]、nums[j] 和 nums[k] 组成，
并同时满足：i < j < k 和 nums[i] < nums[k] < nums[j] 。
如果 nums 中存在 132 模式的子序列 ，返回 true ；否则，返回 false 。

进阶：很容易想到时间复杂度为 O(n^2) 的解决方案，你可以设计一个时间复杂度为 O(n logn) 或 O(n) 的解决方案吗？

示例 1：
输入：nums = [1,2,3,4]
输出：false
解释：序列中不存在 132 模式的子序列。

示例 2：
输入：nums = [3,1,4,2]
输出：true
解释：序列中有 1 个 132 模式的子序列： [1, 4, 2] 。

示例 3：
输入：nums = [-1,3,2,0]
输出：true
解释：序列中有 3 个 132 模式的的子序列：[-1, 3, 2]、[-1, 3, 0] 和 [-1, 2, 0] 。

提示：
n == nums.length
1 <= n <= 104
-109 <= nums[i] <= 109

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/132-pattern
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def find132pattern(self, nums):
        """
        这个方法就是 O(N^2)的解法，是这个题的暴力解法。

        我选择的方法是维护 132模式 中间的那个数字 3，因为 3 在 132 的中间的数字、也是最大的数字。
        我们的思路是个贪心的方法：我们要维护的 1 是 3 左边的最小的数字； 2 是 3 右边的比 3 小并且比 1 大的数字。

        从左到右遍历一次，遍历的数字是nums[j] 也就是 132 模式中的 3。
        根据上面的贪心思想分析，我们想让 1 是 3 左边最小的元素，然后使用暴力在nums[j+1..N−1] 中找到 132 模式中的 2 就行。

        这个思路比较简单，也能 AC。
        """
        N = len(nums)
        numsi = nums[0]
        for j in range(1, N):
            for k in range(N - 1, j, -1):
                if numsi < nums[k] and nums[k] < nums[j]:
                    return True
            numsi = min(numsi, nums[j])
        return False

    def find132pattern(self, nums):
        """
        求任何位置的左边最小的元素 nums[i]，可以提前遍历一次而得到；
        使用「单调递减栈」，把 nums[j] 入栈时，需要把栈里面比它小的元素全都 pop 出来，
        由于越往栈底越大，所以 pop 出的最后一个元素，就是比 3 小的最大元素 nums[k]。
        判断如果 nums[i] < nums[k]，那就说明得到了一个 132 模式。
        因为单调栈是建立在 3 的右边的，因此，我们使用从右向左遍历。
        """
        N = len(nums)
        leftMin = [float("inf")] * N
        for i in range(1, N):
            leftMin[i] = min(leftMin[i - 1], nums[i - 1])
        stack = []
        for j in range(N - 1, -1, -1):
            numsk = float("-inf")
            while stack and stack[-1] < nums[j]:
                numsk = stack.pop()
            if leftMin[j] < numsk:
                return True
            stack.append(nums[j])
        return False
