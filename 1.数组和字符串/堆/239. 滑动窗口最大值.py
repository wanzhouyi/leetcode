"""
给你一个整数数组 nums，有一个大小为k的滑动窗口从数组的最左侧移动到数组的最右侧。
你只可以看到在滑动窗口内的 k个数字。滑动窗口每次只向右移动一位。
返回滑动窗口中的最大值。

示例 1：
输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
输出：[3,3,5,5,6,7]
解释：
滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

示例 2：
输入：nums = [1], k = 1
输出：[1]

示例 3：
输入：nums = [1,-1], k = 1
输出：[1,-1]

示例 4：
输入：nums = [9,11], k = 2
输出：[11]

示例 5：
输入：nums = [4,-2], k = 2
输出：[4]

提示：
1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sliding-window-maximum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    # 方法一，暴力解法，超时
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        for i in range(len(nums) - k + 1):
            result.append(max(nums[i:i + k]))
        return result

    # 方法二，使用sortedlist，1812ms
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        leetcode内置了sortedcontainers，可以使用SortedList
        但是sl的删除元素操作复杂度仍是O(n)，需要继续寻找更优解
        """
        from sortedcontainers import SortedList
        sl = SortedList()
        sl.update(nums[:k])
        n = len(nums)
        result = []
        for i in range(n - k + 1):
            result.append(sl[-1])
            sl.remove(nums[i])
            if i + k < n:
                sl.add(nums[i + k])
        return result
    #方法三，双端队列
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        比较假的双端队列
        """
        from collections import deque
        # 特判
        if not nums:
            return []
        # 滑动窗口，注意：保存的是索引值
        q=deque()
        ans=[]
        for idx,num in enumerate(nums):
            # 当元素从左边界滑出的时候，如果它恰恰好是滑动窗口的最大值
            # 那么将它弹出
            if q and q[0] <= idx- k:
                q.popleft()
            # 如果滑动窗口非空，新进来的数比队列里已经存在的数还要大
            # 则说明已经存在数一定不会是滑动窗口的最大值（它们毫无出头之日）
            # 将它们弹出
            while q and nums[q[-1]]<=num:
                q.pop()
            q.append(idx)
            # 队首一定是滑动窗口的最大值的索引
            if idx >= k - 1:
                ans.append(nums[q[0]])
        return ans
    #方法四，双端队列，官方题解
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        import collections
        n = len(nums)
        q = collections.deque()
        for i in range(k):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)

        ans = [nums[q[0]]]
        for i in range(k, n):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
            while q[0] <= i - k:
                q.popleft()
            ans.append(nums[q[0]])

        return ans
    #方法五，堆，官方题解
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        import heapq
        n = len(nums)
        # 注意 Python 默认的优先队列是小根堆
        q = [(-nums[i], i) for i in range(k)]
        heapq.heapify(q)

        ans = [-q[0][0]]
        for i in range(k, n):
            heapq.heappush(q, (-nums[i], i))
            while q[0][1] <= i - k:
                heapq.heappop(q)
            ans.append(-q[0][0])

        return ans





if __name__ == '__main__':
    s = Solution()
    print(s.maxSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))
    print(s.maxSlidingWindow(nums=[1], k=1))
    print(s.maxSlidingWindow(nums=[1, -1], k=1))
    print(s.maxSlidingWindow(nums=[9, 11], k=2))
    print(s.maxSlidingWindow(nums=[4, -2], k=2))
