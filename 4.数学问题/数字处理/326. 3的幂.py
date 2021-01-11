"""
给定一个整数，写一个函数来判断它是否是 3的幂次方。如果是，返回 true ；否则，返回 false 。
整数 n 是 3 的幂次方需满足：存在整数 x 使得 n == 3x

示例 1：
输入：n = 27
输出：true

示例 2：
输入：n = 0
输出：false

示例 3：
输入：n = 9
输出：true

示例 4：
输入：n = 45
输出：false

提示：

-231 <= n <= 231 - 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/power-of-three
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    # 方法一，系统函数，140 ms，8.53%
    def isPowerOfThree(self, n: int) -> bool:
        import math
        if n <= 0:
            return False
        # 注意是用round
        if 3 ** round(math.log(n, 3)) == n:
            return True
        return False

    # 方法二，迭代，96 ms，59.57%
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        while n != 1:
            if n % 3 != 0:
                return False
            n = n // 3
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isPowerOfThree(27))
    print(s.isPowerOfThree(28))
    print(s.isPowerOfThree(0))
    print(s.isPowerOfThree(9))
    print(s.isPowerOfThree(45))
