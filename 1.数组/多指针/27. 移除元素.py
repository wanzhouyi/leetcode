"""
给你一个数组 nums和一个值 val，你需要 原地 移除所有数值等于val的元素，并返回移除后数组的新长度。
不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

示例 1:
给定 nums = [3,2,2,3], val = 3,
函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。
你不需要考虑数组中超出新长度后面的元素。

示例2:
给定 nums = [0,1,2,2,3,0,4,2], val = 2,
函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。

注意这五个元素可为任意顺序。
你不需要考虑数组中超出新长度后面的元素。

说明:
为什么返回数值是整数，但输出的答案是数组呢?
请注意，输入数组是以「引用」方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。
你可以想象内部操作如下:
// nums 是以“引用”方式传递的。也就是说，不对实参作任何拷贝
int len = removeElement(nums, val);

// 在函数里修改输入数组对于调用者是可见的。
// 根据你的函数返回的长度, 它会打印出数组中 该长度范围内 的所有元素。
for (int i = 0; i < len; i++) {
    print(nums[i]);
}

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-element
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    # 方法一，暴力法，44ms
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        while left < len(nums):
            if nums[left] == val:
                del nums[left]
            else:
                left += 1
        return len(nums)

    # 方法二，双指针，44ms
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        left, right = 0, n - 1
        # 特判
        if n == 1:
            if left == right and nums[left] == val:
                return 0
            else:
                return 1

        while left < right:
            while left <= n - 1 and nums[left] != val:
                left += 1
            while right > 0 and nums[right] == val:
                right -= 1
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
        return left

    # 方法三，同向双指针(快慢指针），32ms
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        left = 0
        for right in range(n):
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1
        return left


if __name__ == '__main__':
    s = Solution()
    print(s.removeElement(nums=[3, 2, 2, 3], val=3))
    print(s.removeElement(nums=[0, 1, 2, 2, 3, 0, 4, 2], val=2))
    # 数组都应该有一个空数组用例
    print(s.removeElement(nums=[], val=3))
    # 数组都应该有一个元素的用例
    print(s.removeElement(nums=[2], val=2))
    print(s.removeElement(nums=[2], val=3))

    # 全部被替换的情况
    print(s.removeElement(nums=[2, 2, 2], val=2))
    # 一个都不被替换的情况
    print(s.removeElement(nums=[2, 2, 2], val=3))
    # 替换一部分的情况
    print(s.removeElement(nums=[2, 2, 3], val=3))
