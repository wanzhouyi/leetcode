"""
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
示例:
输入:n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combinations
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    # 方法一，系统函数，40 ms，99%
    def combine(self, n: int, k: int) -> List[List[int]]:
        from itertools import combinations
        com = combinations(list(range(1, n + 1)), k)
        return [list(x) for x in com]

    # 方法二，回溯，580 ms，15%
    def combine(self, n: int, k: int) -> List[List[int]]:
        ls = [i for i in range(1, n + 1)]
        result = set()

        def back_track(nums, path: list):
            if len(path) == k:
                result.add(tuple(sorted(path)))
                return
            for idx, num in enumerate(nums):
                path.append(num)
                back_track(nums[idx + 1:], path)
                path.pop()

        back_track(ls, [])
        return [list(x) for x in result]


if __name__ == '__main__':
    s = Solution()
    print(s.combine(4, 2))
