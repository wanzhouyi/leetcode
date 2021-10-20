"""
给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。
示例1：
输入：digits = [1,2,3]
输出：[1,2,4]
解释：输入数组表示数字 123。
示例2：
输入：digits = [4,3,2,1]
输出：[4,3,2,2]
解释：输入数组表示数字 4321。
示例 3：

输入：digits = [0]
输出：[1]

提示：

1 <= digits.length <= 100
0 <= digits[i] <= 9

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/plus-one
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = []
        jinwei = 1
        while digits:
            num = digits.pop()
            num += jinwei
            jinwei = 0 if num <= 9 else 1
            ans.append(num if num <= 9 else 0)
        if jinwei == 1:
            ans.append(jinwei)
        return ans[::-1]


class Solution:
    """
    方法一：找出最长的后缀 99
    思路

    当我们对数组 \textit{digits}digits 加一时，我们只需要关注 \textit{digits}digits 的末尾出现了多少个 99 即可。我们可以考虑如下的三种情况：

    如果 \textit{digits}digits 的末尾没有 99，例如 [1, 2, 3][1,2,3]，那么我们直接将末尾的数加一，得到 [1, 2, 4][1,2,4] 并返回；

    如果 \textit{digits}digits 的末尾有若干个 99，例如 [1, 2, 3, 9, 9][1,2,3,9,9]，那么我们只需要找出从末尾开始的第一个不为 99 的元素，即 33，将该元素加一，得到 [1, 2, 4, 9, 9][1,2,4,9,9]。随后将末尾的 99 全部置零，得到 [1, 2, 4, 0, 0][1,2,4,0,0] 并返回。

    如果 \textit{digits}digits 的所有元素都是 99，例如 [9, 9, 9, 9, 9][9,9,9,9,9]，那么答案为 [1, 0, 0, 0, 0, 0][1,0,0,0,0,0]。我们只需要构造一个长度比 \textit{digits}digits 多 11 的新数组，将首元素置为 11，其余元素置为 00 即可。

    算法

    们只需要对数组 \textit{digits}digits 进行一次逆序遍历，找出第一个不为 99 的元素，将其加一并将后续所有元素置零即可。如果 \textit{digits}digits 中所有的元素均为 99，那么对应着「思路」部分的第三种情况，我们需要返回一个新的数组。

    作者：LeetCode-Solution
    链接：https://leetcode-cn.com/problems/plus-one/solution/jia-yi-by-leetcode-solution-2hor/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        for i in range(n - 1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                for j in range(i + 1, n):
                    digits[j] = 0
                return digits

        # digits 中所有的元素均为 9
        return [1] + [0] * n


if __name__ == '__main__':
    s = Solution()
    print(s.plusOne(digits=[1, 2, 3]))
    print(s.plusOne(digits=[9, 9, 9]))
