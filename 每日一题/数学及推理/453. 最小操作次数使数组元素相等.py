"""
给你一个长度为 n 的整数数组，每次操作将会使 n - 1 个元素增加 1 。返回让数组所有元素相等的最小操作次数。

示例 1：

输入：nums = [1,2,3]
输出：3
解释：
只需要3次操作（注意每次操作会增加两个元素的值）：
[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
示例 2：

输入：nums = [1,1,1]
输出：0


提示：

n == nums.length
1 <= nums.length <= 105
-109 <= nums[i] <= 109
答案保证符合 32-bit 整数

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-moves-to-equal-array-elements
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
from sortedcontainers import SortedList


class Solution:
    # 思想正确，但是超时
    def minMoves(self, nums: List[int]) -> int:
        snum = SortedList(nums)
        print(snum)
        print(snum[0], snum[-1])
        ans = 0
        while snum[0] != snum[-1]:
            last = snum.pop()
            snum.add(last - 1)
            print(snum)
            ans += 1
        return ans


class Solution:
    # 沿袭反过来想的思路
    def minMoves(self, nums: List[int]) -> int:
        min_val = min(nums)
        n = len(nums)
        return sum(nums) - min_val * n


if __name__ == '__main__':
    s = Solution()
    print(s.minMoves(nums=[1, 2, 3, 8, 6]))
