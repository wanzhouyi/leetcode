"""
给定一个整数 n，返回 n! 结果尾数中零的数量。

示例 1:

输入: 3
输出: 0
解释:3! = 6, 尾数中没有零。
示例2:

输入: 5
输出: 1
解释:5! = 120, 尾数中有 1 个零.
说明: 你算法的时间复杂度应为O(logn)。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/factorial-trailing-zeroes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def trailingZeroes(self, n: int) -> int:
        result = 1
        for i in range(1, n + 1):
            result *= i

        counter = 0
        result1 = list(str(result))

        while result1:
            if result1.pop() == '0':
                counter += 1
            else:
                break
        return counter


if __name__ == '__main__':
    s = Solution()
    print(s.trailingZeroes(3))
    print(s.trailingZeroes(5))
    print(s.trailingZeroes(0))
    print(s.trailingZeroes(-50))
