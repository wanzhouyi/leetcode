"""
给定一个无重复元素的有序整数数组 nums 。
返回 恰好覆盖数组中所有数字 的 最小有序 区间范围列表。
也就是说，nums 的每个元素都恰好被某个区间范围所覆盖，并且不存在属于某个范围但不属于 nums 的数字 x 。
列表中的每个区间范围 [a,b] 应该按如下格式输出：

"a->b" ，如果 a != b
"a" ，如果 a == b

示例 1：
输入：nums = [0,1,2,4,5,7]
输出：["0->2","4->5","7"]
解释：区间范围是：
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"

示例 2：
输入：nums = [0,2,3,4,6,8,9]
输出：["0","2->4","6","8->9"]
解释：区间范围是：
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"

示例 3：
输入：nums = []
输出：[]

示例 4：
输入：nums = [-1]
输出：["-1"]

示例 5：
输入：nums = [0]
输出：["0"]

提示：

0 <= nums.length <= 20
-231 <= nums[i] <= 231 - 1
nums 中的所有值都 互不相同
nums 按升序排列

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/summary-ranges
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from itertools import groupby
from operator import itemgetter
from typing import List


class Solution:
    # 方法一，模拟，40 ms，51.46%
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        result = []
        n = len(nums)
        left, right = 0, 0
        for right in range(1, n):
            if nums[right] != nums[right - 1] + 1:
                if right - left == 1:
                    result.append(str(nums[left]))
                else:
                    result.append(str(nums[left]) + '->' + str(nums[right - 1]))
                left = right

        if right == left:
            result.append(str(nums[left]))
        else:
            result.append(str(nums[left]) + '->' + str(nums[right]))

        return result

    # 方法二，使用groupby，28 ms，97.17%
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        for k, g in groupby(enumerate(nums), lambda x: x[0] - x[1]):
            ls = list(map(itemgetter(1), g))
            result.append("{}->{}".format(ls[0], ls[-1]) if len(ls) > 1 else str(ls[0]))
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.summaryRanges([0, 1, 2, 4, 5, 7]))
    print(s.summaryRanges([0, 1, 2, 4, 5, 7, 8]))
    print(s.summaryRanges(nums=[0, 2, 3, 4, 6, 8, 9]))
    print(s.summaryRanges([]))
    print(s.summaryRanges([-1]))
    print(s.summaryRanges([0]))

    print(s.summaryRanges([-1, 0, 1]))
