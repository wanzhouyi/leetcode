"""
给定一个已按照升序排列的有序数组，找到两个数使得它们相加之和等于目标数。
函数应该返回这两个下标值 index1 和 index2，其中 index1必须小于index2。

说明:
返回的下标值（index1 和 index2）不是从零开始的。
你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。

示例:
输入: numbers = [2, 7, 11, 15], target = 9
输出: [1,2]
解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    # 方法一，暴力法，2716 ms，5.52%
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for idx, num in enumerate(numbers):
            sub = target - num
            if sub in numbers[idx + 1:]:
                return [idx + 1, idx + numbers[idx + 1:].index(sub) + 2]

    # 方法二，双指针，44 ms，68.37%
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        from operator import add
        left, right = 0, len(numbers) - 1
        while left < right:
            temp_add = add(numbers[left], numbers[right])
            if temp_add > target:
                right -= 1
            elif temp_add < target:
                left += 1
            else:
                return [left + 1, right + 1]


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum(numbers=[2, 7, 11, 15], target=9))
    print(s.twoSum(numbers=[2, 7, 11, 15], target=18))
    print(s.twoSum(numbers=[2, 7, 11, 15], target=22))
    print(s.twoSum(numbers=[2, 11, 11, 15], target=22))
