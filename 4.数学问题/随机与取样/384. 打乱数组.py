"""
给你一个整数数组 nums ，设计算法来打乱一个没有重复元素的数组。
实现 Solution class:
Solution(int[] nums) 使用整数数组 nums 初始化对象
int[] reset() 重设数组到它的初始状态并返回
int[] shuffle() 返回数组随机打乱后的结果
示例：
输入
["Solution", "shuffle", "reset", "shuffle"]
[[[1, 2, 3]], [], [], []]
输出
[null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]

解释
Solution solution = new Solution([1, 2, 3]);
solution.shuffle();    // 打乱数组 [1,2,3] 并返回结果。任何 [1,2,3]的排列返回的概率应该相同。例如，返回 [3, 1, 2]
solution.reset();      // 重设数组到它的初始状态 [1, 2, 3] 。返回 [1, 2, 3]
solution.shuffle();    // 随机返回数组 [1, 2, 3] 打乱后的结果。例如，返回 [1, 3, 2]

提示：

1 <= nums.length <= 200
-106 <= nums[i] <= 106
nums 中的所有元素都是 唯一的
最多可以调用 5 * 104 次 reset 和 shuffle

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shuffle-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import random
from typing import List
from random import sample


# 系统函数
class Solution:

    def __init__(self, nums: List[int]):
        self.source = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.source

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        return sample(self.source, len(self.source))


# 洗牌算法
class Solution:
    def __init__(self, nums):
        self.array = nums
        self.original = list(nums)

    def reset(self):
        self.array = self.original
        self.original = list(self.original)
        return self.array

    def shuffle(self):
        for i in range(len(self.array)):
            swap_idx = random.randrange(i, len(self.array))
            self.array[i], self.array[swap_idx] = self.array[swap_idx], self.array[i]
        return self.array


if __name__ == '__main__':
    s = Solution([1, 2, 3])
    print(s.shuffle())
    print(s.reset())
    print(s.shuffle())
