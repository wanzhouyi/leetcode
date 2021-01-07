"""
给定一个数组，将数组中的元素向右移动k个位置，其中k是非负数。

示例 1:
输入: [1,2,3,4,5,6,7] 和 k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]

示例2:

输入: [-1,-100,3,99] 和 k = 2
输出: [3,99,-1,-100]
解释: 
向右旋转 1 步: [99,-1,-100,3]
向右旋转 2 步: [3,99,-1,-100]
说明:

尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
要求使用空间复杂度为O(1) 的原地算法。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rotate-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    # 方法一，数组切片法，36 ms，91.27%
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return []
        n = len(nums)
        k = k % n
        temp = nums[n - k:]
        nums[k:] = nums[:n - k]
        nums[:k] = temp
        print(nums)

    # 方法二，逐位移，1556 ms ms，5.61%
    def rotate(self, nums: List[int], k: int) -> None:
        if not nums:
            return []
        n = len(nums)
        k = k % n
        times = 0
        while times < k:
            times += 1
            nums[:] = [nums[-1]] + nums[:n - 1]

    # 方法三，inert，128 ms，20.50%
    def rotate(self, nums: List[int], k: int) -> None:
        if not nums:
            return []
        n = len(nums)
        k = k % n
        times = 0
        while times < k:
            times += 1
            nums.insert(0, nums.pop())

        return nums


if __name__ == '__main__':
    s = Solution()
    print(s.rotate([1, 2, 3, 4, 5, 6, 7], k=3))
    print(s.rotate([-1, -100, 3, 99], k=2))
    # 空数组
    print(s.rotate([], 2))
    # 单数组
    print(s.rotate([1], 0))
    print(s.rotate([1], 1))
    print(s.rotate([1], 2))
    # 双数组
    print(s.rotate([1, 2], 3))
