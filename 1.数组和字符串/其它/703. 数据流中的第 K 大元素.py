"""
设计一个找到数据流中第 k 大元素的类（class）。注意是排序后的第 k 大元素，不是第 k 个不同的元素。

请实现 KthLargest类：

KthLargest(int k, int[] nums) 使用整数 k 和整数流 nums 初始化对象。
int add(int val) 将 val 插入数据流 nums 后，返回当前数据流中第 k 大的元素。

示例：

输入：
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
输出：
[null, 4, 5, 5, 8, 8]

解释：
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8

提示：
1 <= k <= 104
0 <= nums.length <= 104
-104 <= nums[i] <= 104
-104 <= val <= 104
最多调用 add 方法 104 次
题目数据保证，在查找第 k 大元素时，数组中至少有 k 个元素

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/kth-largest-element-in-a-stream
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
import bisect


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.stack = sorted(nums)
        self.k = k

    def add(self, val: int) -> int:
        bisect.insort_left(self.stack, val)
        return self.stack[-self.k]


import heapq


class KthLargest:
    def __init__(self, k, nums):
        # self k
        self.k = k
        self.heap = nums
        # heap其实就是个list
        heapq.heapify(self.heap)
        # 减小到k
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val):
        # 堆不够，则直接添加进去
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif self.heap[0] < val:
            # 新的值更大，更新
            heapq.heapreplace(self.heap, val)

        return self.heap[0]


if __name__ == '__main__':
    kthLargest = KthLargest(3, [4, 5, 8, 2])
    print(kthLargest.add(3))  # return 4
    print(kthLargest.add(5))  # return 5
    print(kthLargest.add(10))  # return 5
    print(kthLargest.add(9))  # return 8
    print(kthLargest.add(4))  # return 8
