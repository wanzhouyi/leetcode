"""
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:
输入: [3,2,1,5,6,4] 和 k = 2
输出: 5

示例2:
输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
说明:

你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/kth-largest-element-in-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    # 方法一，排序，48 ms，66.37%
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[len(nums) - k]

    # 方法二，堆排序，40 ms，89.77%
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        hp = nums[:k]
        heapq.heapify(hp)
        for num in nums[k:]:
            heapq.heappushpop(hp, num)
        return hp[0]


if __name__ == '__main__':
    s = Solution()
    print(s.findKthLargest([3, 2, 1, 5, 6, 4], k=2))
    print(s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], k=4))
