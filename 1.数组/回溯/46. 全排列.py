"""
给定一个 没有重复 数字的序列，返回其所有可能的全排列。
示例:
输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutations
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    # 方法一，利用系统函数，40ms，74%
    def permute(self, nums: List[int]) -> List[List[int]]:
        from itertools import permutations
        return [list(x) for x in permutations(nums)]

    # 方法二，回溯，44ms，51%
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def back_track(ls, path):
            if not ls:
                result.append(path.copy())
                return
            for idx, num in enumerate(ls):
                path.append(num)
                back_track(ls[:idx] + ls[idx + 1:], path)
                path.pop()

        back_track(nums, [])
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.permute([1, 2, 3]))
