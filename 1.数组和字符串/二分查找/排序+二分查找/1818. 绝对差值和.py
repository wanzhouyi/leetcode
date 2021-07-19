"""
给你两个正整数数组 nums1 和 nums2 ，数组的长度都是 n 。
数组 nums1 和 nums2 的 绝对差值和 定义为所有 |nums1[i] - nums2[i]|（0 <= i < n）的 总和（下标从 0 开始）。
你可以选用 nums1 中的 任意一个 元素来替换 nums1 中的 至多 一个元素，以 最小化 绝对差值和。
在替换数组 nums1 中最多一个元素 之后 ，返回最小绝对差值和。因为答案可能很大，所以需要对 109 + 7 取余 后返回。
|x| 定义为：
如果 x >= 0 ，值为 x ，或者
如果 x <= 0 ，值为 -x
示例 1：
输入：nums1 = [1,7,5], nums2 = [2,3,5]
输出：3
解释：有两种可能的最优方案：
- 将第二个元素替换为第一个元素：[1,7,5] => [1,1,5] ，或者
- 将第二个元素替换为第三个元素：[1,7,5] => [1,5,5]
两种方案的绝对差值和都是 |1-2| + (|1-3| 或者 |5-3|) + |5-5| = 3
示例 2：
输入：nums1 = [2,4,6,8,10], nums2 = [2,4,6,8,10]
输出：0
解释：nums1 和 nums2 相等，所以不用替换元素。绝对差值和为 0
示例 3：
输入：nums1 = [1,10,4,4,2,7], nums2 = [9,3,5,1,7,4]
输出：20
解释：将第一个元素替换为第二个元素：[1,10,4,4,2,7] => [10,10,4,4,2,7]
绝对差值和为 |10-9| + |10-3| + |4-5| + |4-1| + |2-7| + |7-4| = 20


提示：

n == nums1.length
n == nums2.length
1 <= n <= 10^5
1 <= nums1[i], nums2[i] <= 10^5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-absolute-sum-difference
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from bisect import bisect
from typing import List


class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        chazhi = [abs(nums1[i] - nums2[i]) for i in range(n)]
        sum_chazhi = sum(chazhi)
        # print(chazhi)
        nums1_copy = sorted(nums1)
        # print(nums1_copy)
        ans = sum_chazhi
        for i in range(n):
            idx = bisect.bisect_left(nums1_copy, nums2[i])
            if idx == 0:
                ans = min(ans, sum_chazhi - chazhi[i] + abs(nums2[i] - nums1_copy[0]))
            elif idx == n:
                ans = min(ans, sum_chazhi - chazhi[i] + abs(nums2[i] - nums1_copy[-1]))
            else:
                ans = min(ans, sum_chazhi - chazhi[i] + abs(nums2[i] - nums1_copy[idx]),
                          sum_chazhi - chazhi[i] + abs(nums2[i] - nums1_copy[idx - 1]))
        return ans % (10 ** 9 + 7)


class Solution1:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        # 二分查找,找第一个大于等于targe的数
        def find_big(nums, target):
            l, r = 0, len(nums) - 1
            while l < r:
                mid = l + (r - l) // 2
                if nums[mid] > target:
                    r = mid
                elif nums[mid] == target:
                    return mid
                else:
                    l = mid + 1
            return r

        n = len(nums1)
        abs_all = 0
        # 1. 先求绝对差值和
        for i in range(n):
            abs_all += abs(nums1[i] - nums2[i])
        # print(abs_all)
        nums = sorted(nums1)
        # 2. 再二分找改变
        abs_all_tem = abs_all
        for i in range(n):
            target = nums2[i]
            index_mid = find_big(nums, target)
            change_num = nums[index_mid]
            # 2.2 找到与targe相等的值，则不需要找第一个大和第一个小
            if change_num == target:
                abs_ll_equal = abs_all - abs(nums1[i] - nums2[i]) + abs(change_num - nums2[i])
                abs_all_tem = min(abs_all_tem, abs_ll_equal)
            # 2.3 此时返回的是第一个大于target的数
            else:
                # 2.3.1 计算第一个大于targe的数
                abs_all_big = abs_all - abs(nums1[i] - nums2[i]) + abs(change_num - nums2[i])

                # 2.3.2 找第一个小于target的数
                if index_mid > 0:
                    abs_all_small = abs_all - abs(nums1[i] - nums2[i]) + abs(
                        nums[index_mid - 1] - nums2[i])
                    abs_all_tem = min(abs_all_tem, abs_all_big, abs_all_small)
                else:
                    abs_all_tem = min(abs_all_tem, abs_all_big)
            # print(abs_all)
        return abs_all_tem % (10 ** 9 + 7)


if __name__ == '__main__':
    s = Solution()
    print(s.minAbsoluteSumDiff(nums1=[1, 7, 5], nums2=[2, 3, 5]))
    print(s.minAbsoluteSumDiff(nums1=[2, 4, 6, 8, 10], nums2=[2, 4, 6, 8, 10]))
    print(s.minAbsoluteSumDiff(nums1=[1, 10, 4, 4, 2, 7], nums2=[9, 3, 5, 1, 7, 4]))
    print(s.minAbsoluteSumDiff([1, 28, 21], [9, 21, 20]))
    print(s.minAbsoluteSumDiff(
        [57, 42, 21, 28, 30, 25, 22, 12, 55, 3, 47, 18, 43, 29, 20, 44, 59, 9, 43, 7, 8, 5, 42, 53,
         99, 34, 37, 88, 87, 62, 38, 68, 31, 3, 11, 61, 93, 34, 63, 27, 20, 48, 38, 5, 71, 100, 88,
         54, 52, 15, 98, 59, 74, 26, 81, 38, 11, 44, 25, 69, 79, 81, 51, 85, 59, 84, 83, 99, 31, 47,
         31, 23, 83, 70, 82, 79, 86, 31, 50, 17, 11, 100, 55, 15, 98, 11, 90, 16, 46, 89, 34, 33,
         57, 53, 82, 34, 25, 70, 5, 1],
        [76, 3, 5, 29, 18, 53, 55, 79, 30, 33, 87, 3, 56, 93, 40, 80, 9, 91, 71, 38, 35, 78, 32, 58,
         77, 41, 63, 5, 21, 67, 21, 84, 52, 80, 65, 38, 62, 99, 80, 13, 59, 94, 21, 61, 43, 82, 29,
         97, 31, 24, 95, 52, 90, 92, 37, 26, 65, 89, 90, 32, 27, 3, 42, 47, 93, 25, 14, 5, 39, 85,
         89, 7, 74, 38, 12, 46, 40, 25, 51, 2, 19, 8, 21, 62, 58, 29, 32, 77, 62, 9, 74, 98, 10, 55,
         25, 62, 48, 48, 24, 21]))
