"""
给定一个范围在 1 ≤ a[i] ≤ n (n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。
找到所有在 [1, n] 范围之间没有出现在数组中的数字。
您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。
示例:
输入:
[4,3,2,7,8,2,3,1]
输出:
[5,6]
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-all-numbers-disappeared-in-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    # 方法一，集合求差集，340 ms，99.17%
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s1 = set(list(range(1, len(nums) + 1)))
        s2 = set(nums)
        return list(s1.difference(s2))
    # 方法二，哈希表
    # 方法三，集合遍历


if __name__ == '__main__':
    s = Solution()
    print(s.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
