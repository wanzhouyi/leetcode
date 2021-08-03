"""
给定一个包含非负整数的数组，你的任务是统计其中可以组成三角形三条边的三元组个数。

示例 1:

输入: [2,2,3,4]
输出: 3
解释:
有效的组合是:
2,3,4 (使用第一个 2)
2,3,4 (使用第二个 2)
2,2,3
注意:

数组长度不超过1000。
数组里整数的范围为 [0, 1000]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-triangle-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
import bisect


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        ans = 0
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                idx = bisect.bisect_left(nums, nums[i] + nums[j], j)
                if idx == n:
                    ans += (n - j - 1)
                elif j < idx < n:
                    ans += (idx - j - 1)
        return ans


# 官解
class Solution:
    """
    方法一：排序 + 二分查找
    思路与算法
    对于正整数 a, b, c，它们可以作为三角形的三条边，当且仅当：
    a+b>c
    a+c>b
    b+c>a
    均成立。如果我们将三条边进行升序排序，使它们满足 a≤b≤c，那么 a + c > b 和 b + c > a 使一定成立的，
    我们只需要保证 a + b > c。
    因此，我们可以将数组 nums 进行升序排序，随后使用二重循环枚举 a 和 b。设 a=nums[i],b=nums[j]，
    为了防止重复统计答案，我们需要保证 i < j。剩余的边 c 需要满足 c<nums[i]+nums[j]，
    我们可以在 [j + 1, n - 1] 的下标范围内使用二分查找（其中 n 是数组nums 的长度），
    找出最大的满足 nums[k]<nums[i]+nums[j] 的下标 k，这样一来，在 [j + 1, k] 范围内的下标都可以作为边 c 的下标，
    我们将该范围的长度 k - j累加入答案。

    当枚举完成后，我们返回累加的答案即可。

    细节

    注意到题目描述中 nums 包含的元素为非负整数，即除了正整数以外，nums 还会包含0。
    但如果我们将nums 进行升序排序，那么在枚举 a 和 b 时出现了 0，那么 nums[i] 一定为 0。
    此时，边 c 需要满足 c<nums[i]+nums[j]=nums[j]，
    而下标在 [j + 1, n - 1]范围内的元素一定都是大于等于 nums[j] 的，
    因此二分查找会失败。若二分查找失败，我们可以令 k = j，此时对应的范围长度 k - j = 0，我们也就保证了答案的正确性。

    作者：LeetCode-Solution
    链接：https://leetcode-cn.com/problems/valid-triangle-number/solution/you-xiao-san-jiao-xing-de-ge-shu-by-leet-t2td/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                left, right, k = j + 1, n - 1, j
                while left <= right:
                    mid = (left + right) // 2
                    if nums[mid] < nums[i] + nums[j]:
                        k = mid
                        left = mid + 1
                    else:
                        right = mid - 1
                ans += k - j
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.triangleNumber([2, 2, 3, 4]))
