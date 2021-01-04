"""
给你两个有序整数数组nums1 和 nums2，请你将 nums2 合并到nums1中，使 nums1 成为一个有序数组。

说明：
初始化nums1 和 nums2 的元素数量分别为m 和 n 。
你可以假设nums1有足够的空间（空间大小大于或等于m + n）来保存 nums2 中的元素。

示例：
输入：
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3
输出：[1,2,2,3,5,6]

提示：
-10^9 <= nums1[i], nums2[i] <= 10^9
nums1.length == m + n
nums2.length == n

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    # 方法一，使用额外数组+双指针，44 ms，33.39%
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        shadow_nums1 = nums1[:m]
        i, j = 0, 0
        idx = 0
        while i < m and j < n:
            if shadow_nums1[i] > nums2[j]:
                nums1[idx] = nums2[j]
                j += 1
            else:
                nums1[idx] = shadow_nums1[i]
                i += 1
            idx += 1
        if i < m:
            nums1[idx:idx + m - i] = shadow_nums1[i:]
        if j < n:
            nums1[idx:idx + n - j] = nums2[j:]

    # 方法二，使用系统函数，36 ms，81.89%
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        new_arr = nums1[:m] + nums2
        new_arr.sort()
        nums1[:m + n] = new_arr


if __name__ == '__main__':
    s = Solution()
    print(s.merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3))
