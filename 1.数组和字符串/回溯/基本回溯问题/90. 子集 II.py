"""
给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。
解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。

示例 1：
输入：nums = [1,2,2]
输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]
示例 2：
输入：nums = [0]
输出：[[],[0]]

提示：

1 <= nums.length <= 10
-10 <= nums[i] <= 10

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subsets-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        from sortedcontainers import SortedList
        check = SortedList()
        ans = set()

        def back_track(ls: list):
            ans.add(tuple(check))
            if not ls:
                return
            for i in range(len(ls)):
                check.add(ls[i])
                if tuple(check) not in ans:
                    back_track(ls[:i] + ls[i + 1:])
                check.discard(ls[i])

        back_track(nums)
        return list(map(list, ans))


class Solution(object):
    """
    首先，要保证不重复，那么在每一层展开的时候需要保证后一个节点不等于前一个节点，不然必定重复。
    因此为了判定后一个节点会不会等于前一个节点，我们需要将原始的输入序列排序。接下来就是树的先根遍历。
    子集问题要的是树的全部节点，排列问题要得是树的叶子节点。大家可以下去多做做这样的题。
    """

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        path = []
        res = []

        def recur(num, path):
            res.append(list(path))  # 搜集各个路径上的点，所以在进入就开始添加到结果中
            if len(num) == 0:
                return
            for i in range(len(num)):
                if i > 0 and num[i] == num[i - 1]:
                    continue
                path.append(num[i])
                recur(num[i + 1:], path)
                path.pop()

        nums.sort()
        recur(nums, path)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.subsetsWithDup(nums=[1, 2, 2]))
    print(s.subsetsWithDup(nums=[0]))
