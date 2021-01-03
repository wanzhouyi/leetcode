"""
给定两个数组，编写一个函数来计算它们的交集。

示例 1：
输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2]

示例 2：
输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[9,4]

说明：
输出结果中的每个元素一定是唯一的。
我们可以不考虑输出结果的顺序。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/intersection-of-two-arrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    # 方法一，使用集合求交集，40ms
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1, s2 = set(nums1), set(nums2)
        return list(s1.intersection(s2))

    # 方法二，排序大法，60ms
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        ans = set()
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] == nums2[j]:
                ans.add(nums1[i])
                i += 1
                j += 1
        return list(ans)


if __name__ == '__main__':
    s = Solution()
    print(s.intersection(nums1=[1, 2, 2, 1], nums2=[2, 2]))
    print(s.intersection(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4]))
