"""
给定一个整数数组A，坡是元组(i, j)，其中i < j且A[i] <= A[j]。这样的坡的宽度为j - i。
找出A中的坡的最大宽度，如果不存在，返回 0 。

示例 1：
输入：[6,0,8,2,1,5]
输出：4
解释：
最大宽度的坡为 (i, j) = (1, 5): A[1] = 0 且 A[5] = 5.
示例 2：
输入：[9,8,1,0,1,9,4,0,4,1]
输出：7
解释：
最大宽度的坡为 (i, j) = (2, 9): A[2] = 1 且 A[9] = 1.
提示：

2 <= A.length <= 50000
0 <= A[i] <= 50000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-width-ramp
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    # 超时
    def maxWidthRamp(self, nums: List[int]) -> int:
        arr = []  # 排序数组
        import bisect
        n = len(nums)
        result = 0
        for idx in range(n - 1, -1, -1):
            if not arr:
                arr.append((nums[idx], idx))
            else:
                idx_new = bisect.bisect_left(arr, (nums[idx], idx))
                arr_new = arr[idx_new:]
                if arr_new:
                    temp = max(arr[idx_new:], key=lambda x: x[1])
                    result = max(result, temp[1] - idx)
                bisect.insort(arr, (nums[idx], idx))
        return result

    def maxWidthRamp(self, nums: List[int]) -> int:
        """
        1 维护一个单调递减栈，其中第一个元素是A中第一个元素，最后一个元素是A的最小值。由于需要计算长度，所以栈中存储A的索引。

        2 从后向前遍历A，当元素大于栈顶元素时，计算一次最大宽度坡，并弹出(因为再往前面遍历宽度肯定会减少)，由于当栈顶索引等于当前遍历到的元素的索引时，肯定会被弹出，所以没有必要判断栈顶索引是否小于等于当前遍历到的索引。

        作者：Elmer
        链接：https://leetcode-cn.com/problems/maximum-width-ramp/solution/dan-diao-zhan-python-yi-kan-jiu-dong-by-elmer/
        来源：力扣（LeetCode）
        著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        """
        stack = []
        n = len(nums)
        for i in range(n):
            if not stack or nums[stack[-1]] > nums[i]:
                stack.append(i)

        res = 0
        i = n - 1
        while i > res:  # 当res大于等于i时没必要继续遍历了
            while stack and nums[stack[-1]] <= nums[i]:
                res = max(res, i - stack[-1])
                stack.pop()
            i -= 1

        return res


class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        for idx, num in enumerate(nums):
            if not stack or nums[stack[-1]] > num:
                stack.append(idx)
        n = len(nums)
        ans = float('-inf')
        for idx in range(n - 1, -1, -1):
            while stack and nums[idx] >= nums[stack[-1]]:
                ans = max(ans, idx - stack[-1])
                stack.pop()
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.maxWidthRamp([6, 0, 8, 2, 1, 5]))
    # print(s.maxWidthRamp([9,8,1,0,1,9,4,0,4,1]))
