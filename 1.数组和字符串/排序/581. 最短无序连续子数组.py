"""
给你一个整数数组 nums ，你需要找出一个 连续子数组 ，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。

请你找出符合题意的 最短 子数组，并输出它的长度。



示例 1：

输入：nums = [2,6,4,8,10,9,15]
输出：5
解释：你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。
示例 2：

输入：nums = [1,2,3,4]
输出：0
示例 3：

输入：nums = [1]
输出：0


提示：

1 <= nums.length <= 104
-105 <= nums[i] <= 105

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        nums_sort = sorted(nums)
        left, right = -1, n
        for i in range(n):
            if nums[i] == nums_sort[i]:
                left = i
            else:
                break
        for j in range(n - 1, -1, -1):
            if nums[j] == nums_sort[j]:
                right = j
            else:
                break
        if left >= right:
            return 0
        else:
            return right - left - 1


class Solution:
    """
    方法一：排序
    思路与算法
    我们将给定的数组 nums 表示为三段子数组拼接的形式，分别记作numsA,numsB，numsC。
    当我们对 numsB进行排序，整个数组将变为有序。换而言之，当我们对整个序列进行排序，numsA和 numsC都不会改变。

    本题要求我们找到最短的numsB，即找到最大的numsA和numsC的长度之和。
    因此我们将原数组 nums 排序与原数组进行比较，取最长的相同的前缀为 numsA ，取最长的相同的后缀为 numsC
     ，这样我们就可以取到最短的 numsB。

    具体地，我们创建数组 nums 的拷贝，记作数组numsSorted，并对该数组进行排序，
    然后我们从左向右找到第一个两数组不同的位置，即为numsB的左边界。同理也可以找到numsB右边界。
    最后我们输出numsB的长度即可。

    特别地，当原数组有序时，numsB的长度为 0，我们可以直接返回结果。

    作者：LeetCode-Solution
    链接：https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray/solution/zui-duan-wu-xu-lian-xu-zi-shu-zu-by-leet-yhlf/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        def isSorted() -> bool:
            for i in range(1, n):
                if nums[i - 1] > nums[i]:
                    return False
            return True

        if isSorted():
            return 0

        numsSorted = sorted(nums)
        left = 0
        while nums[left] == numsSorted[left]:
            left += 1

        right = n - 1
        while nums[right] == numsSorted[right]:
            right -= 1

        return right - left + 1


if __name__ == '__main__':
    s = Solution()
    print(s.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))
    print(s.findUnsortedSubarray(nums=[1, 2, 3, 4]))
    print(s.findUnsortedSubarray(nums=[4, 3, 2, 1]))
    print(s.findUnsortedSubarray(nums=[1]))
    print(s.findUnsortedSubarray(nums=[1, 3, 2, 2, 2]))
