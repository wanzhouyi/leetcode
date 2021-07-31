"""
给你一个整数num，请你找出同时满足下面全部要求的两个整数：

两数乘积等于 num + 1或num + 2
以绝对差进行度量，两数大小最接近
你可以按任意顺序返回这两个整数。

示例 1：

输入：num = 8
输出：[3,3]
解释：对于 num + 1 = 9，最接近的两个因数是 3 & 3；对于 num + 2 = 10, 最接近的两个因数是 2 & 5，因此返回 3 & 3 。
示例 2：

输入：num = 123
输出：[5,25]
示例 3：

输入：num = 999
输出：[40,25]

提示：

1 <= num <= 10^9

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/closest-divisors
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import math
from typing import List


class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        import math
        def get_ele(source: int):
            sqrt_num = math.ceil(math.sqrt(source))
            while sqrt_num > 0:
                if source % sqrt_num == 0:
                    return [sqrt_num, source // sqrt_num]
                sqrt_num -= 1

        ele1 = get_ele(num + 1)
        ele2 = get_ele(num + 2)
        return ele1 if ele1[1] - ele1[0] < ele2[1] - ele2[0] else ele2


class Solution:
    """
    方法二：以平方根为起点遍历因数
    观察问题性质可知，对任意一个在 [\sqrt n, n]范围内的因数，一定有一个与其对称的在 [1, \sqrt n]范围内的因数。
    因此，遍历因数只需要遍历 [1, \sqrt n] 范围即可。
    另外，当 [1, \sqrt n]范围内的因数最大时，与其对称的 [\sqrt n, n]范围内的因数也最小，
    此时这两个数字之间的差值一定是所有可能性中最小的。因此，我们只需要找到 [1, \sqrt n]中的最大因数即可停止。

    作者：LeetCode-Solution
    链接：https://leetcode-cn.com/problems/closest-divisors/solution/zui-jie-jin-de-yin-shu-by-leetcode-solution/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def divide(self, n):
        for i in range(int(math.sqrt(n)), 0, -1):
            if n % i == 0:
                return [i, n // i]

    def closestDivisors(self, num: int) -> List[int]:
        ans = [0, int(1e9)]
        for i in range(num + 1, num + 3):
            cur = self.divide(i)
            if abs(cur[0] - cur[1]) < abs(ans[0] - ans[1]):
                ans = cur
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.closestDivisors(num=8))
    print(s.closestDivisors(num=123))
    print(s.closestDivisors(num=999))
    print(s.closestDivisors(10 ** 9))
