"""
符合下列属性的数组 arr 称为 山峰数组（山脉数组） ：
arr.length >= 3
存在 i（0 < i< arr.length - 1）使得：
arr[0] < arr[1] < ... arr[i-1] < arr[i]
arr[i] > arr[i+1] > ... > arr[arr.length - 1]
给定由整数组成的山峰数组 arr ，返回任何满足 arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1] 的下标 i，即山峰顶部。

示例 1：
输入：arr = [0,1,0]
输出：1
示例 2：
输入：arr = [1,3,5,4,2]
输出：2
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

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/B1IidL
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        for idx, num in enumerate(arr):
            if idx == 0: continue
            if arr[idx - 1] < num > arr[idx + 1]:
                return idx


class Solution:
    """
    方法二：二分查找
思路与算法
记满足题目要求的下标 i 为 i_ans
 。我们可以发现：
当 i < i_ans时，arr[i]< arr[i+1]恒成立；
当 i >i_ans时，arr[i]> arr[i+1]恒成立。
这与方法一的遍历过程也是一致的，因此 i_ans
  即为「最小的满足的下标 ii」，我们可以用二分查找的方法来找出 i_ans

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/B1IidL/solution/shan-feng-shu-zu-de-ding-bu-by-leetcode-9j8lk/
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


if __name__ == '__main__':
    s = Solution()
    print(s.peakIndexInMountainArray(arr=[0, 1, 0]))
