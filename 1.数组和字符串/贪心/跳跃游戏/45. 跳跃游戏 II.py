"""
给定一个非负整数数组，你最初位于数组的第一个位置。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
你的目标是使用最少的跳跃次数到达数组的最后一个位置。
假设你总是可以到达数组的最后一个位置。

示例 1:
输入: [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
    从下标为 0 跳到下标为 1 的位置，跳1步，然后跳3步到达数组的最后一个位置。
示例 2:
输入: [2,3,0,1,4]
输出: 2
提示:
1 <= nums.length <= 1000
0 <= nums[i] <= 10^5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/jump-game-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        steps = 0
        stack = [0]
        visited = set()
        target = len(nums) - 1
        while stack:

            shadow_stack = stack.copy()
            stack.clear()

            for pos in shadow_stack:
                if pos == target:
                    return steps
                if pos in visited:
                    continue
                visited.add(pos)
                for num in range(nums[pos] + 1):
                    stack.append(num + pos)

            steps += 1


class Solution:
    """
    方法二：正向查找可到达的最大位置
    方法一虽然直观，但是时间复杂度比较高，有没有办法降低时间复杂度呢？
    如果我们「贪心」地进行正向查找，每次找到可到达的最远位置，就可以在线性时间内得到最少的跳跃次数。
    例如，对于数组 [2,3,1,2,4,2,3]，初始位置是下标 0，从下标 0 出发，最远可到达下标 2。
    下标 0 可到达的位置中，下标 1 的值是 3，从下标 1 出发可以达到更远的位置，因此第一步到达下标 1。
    从下标 1 出发，最远可到达下标 4。
    下标 1 可到达的位置中，下标 4 的值是 4 ，从下标 4 出发可以达到更远的位置，因此第二步到达下标 4。
    在具体的实现中，我们维护当前能够到达的最大下标位置，记为边界。
    我们从左到右遍历数组，到达边界时，更新边界并将跳跃次数增加 1。

    在遍历数组时，我们不访问最后一个元素，这是因为在访问最后一个元素之前，我们的边界一定大于等于最后一个位置，
    否则就无法跳到最后一个位置了。
    如果访问最后一个元素，在边界正好为最后一个位置的情况下，我们会增加一次「不必要的跳跃次数」，
    因此我们不必访问最后一个元素。

    作者：LeetCode-Solution
    链接：https://leetcode-cn.com/problems/jump-game-ii/solution/tiao-yue-you-xi-ii-by-leetcode-solution/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        maxPos = 0  # 目前能跳到的最远位置
        end = 0  # 上次跳跃可达范围右边界（下次的最右起跳点）
        step = 0  # 跳跃次数
        for i in range(n - 1):
            if maxPos >= i:
                maxPos = max(maxPos, i + nums[i])
                if i == end:  # 到达上次跳跃能到达的右边界了,更新边界并将跳跃次数增加 1。
                    end = maxPos  # 目前能跳到的最远位置变成了下次起跳位置的有边界
                    step += 1  # 进入下一次跳跃
        return step


if __name__ == '__main__':
    s = Solution()
    print(s.jump([2, 3, 1, 1, 4]))
    # print(s.jump([2, 3, 0, 1, 4]))
    # print(s.jump([2,3,1]))
    # print(s.jump([0]))
