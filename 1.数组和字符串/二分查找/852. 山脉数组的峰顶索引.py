"""
符合下列属性的数组 arr 称为 山脉数组 ：
arr.length >= 3
存在 i（0 < i< arr.length - 1）使得：
arr[0] < arr[1] < ... arr[i-1] < arr[i]
arr[i] > arr[i+1] > ... > arr[arr.length - 1]
给你由整数组成的山脉数组 arr ，
返回任何满足 arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1] 的下标 i 。

示例 1：
输入：arr = [0,1,0]
输出：1

示例 2：
输入：arr = [0,2,1,0]
输出：1

示例 3：
输入：arr = [0,10,5,2]
输出：1

示例 4：
输入：arr = [3,4,5,1]
输出：2

示例 5：
输入：arr = [24,69,100,99,79,78,67,36,26,19]
输出：2

提示：

3 <= arr.length <= 104
0 <= arr[i] <= 106
题目数据保证 arr 是一个山脉数组

进阶：很容易想到时间复杂度 O(n) 的解决方案，你可以设计一个 O(log(n)) 的解决方案吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/peak-index-in-a-mountain-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        """
        非常暴力，毫无美感
        """
        pre = -1
        for idx, num in enumerate(arr):
            if num > pre:
                pre = num
            else:
                return idx - 1


class Solution:
    """
    方法二：二分查找
思路与算法
i_ans即为「最小的满足arr_i>arr_i+1的下标 i」，我们可以用二分查找的方法来找出 i_ans。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/peak-index-in-a-mountain-array/solution/shan-mai-shu-zu-de-feng-ding-suo-yin-by-dtqvv/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        left, right, ans = 1, n - 2, 0

        while left <= right:
            mid = (left + right) // 2
            if arr[mid] > arr[mid + 1]:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans
