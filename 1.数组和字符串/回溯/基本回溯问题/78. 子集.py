"""
给你一个整数数组nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。

示例 1：
输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

示例 2：
输入：nums = [0]
输出：[[],[0]]

提示：

1 <= nums.length <= 10
-10 <= nums[i] <= 10
nums 中的所有元素 互不相同

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subsets
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = set()

        def back_track(nums: list, path: list):
            p = path.copy()
            p.sort()
            ans.add(tuple(p))
            if not nums:
                return
            for i in range(len(nums)):
                path.append(nums[i])
                back_track(nums[:i] + nums[i + 1:], path)
                path.pop()

        back_track(nums, [])
        return list(map(list, ans))


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        from sortedcontainers import SortedSet
        nums.sort()
        ans = set()
        check = SortedSet()

        def back_track(nums: list):
            p = check.copy()
            print(p)
            ans.add(tuple(p))
            if not nums:
                return
            for i in range(len(nums)):
                check.add(nums[i])
                if tuple(check) not in ans:
                    back_track(nums[:i] + nums[i + 1:])
                check.discard(nums[i])

        back_track(nums)
        return list(map(list, ans))


class Solution:
    """库函数法"""

    def subsets(self, nums: List[int]) -> List[List[int]]:
        from itertools import combinations
        ans = []
        for r in range(len(nums) + 1):
            ans.extend(list(combinations(nums, r)))
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.subsets(nums=[1, 2, 3]))
    # print(s.subsets(nums=[0]))
