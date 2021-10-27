"""
给定正整数 N，我们按任何顺序（包括原始顺序）将数字重新排序，注意其前导数字不能为零。
如果我们可以通过上述方式得到2 的幂，返回 true；否则，返回 false。
示例 1：
输入：1
输出：true
示例 2：
输入：10
输出：false
示例 3：
输入：16
输出：true
示例 4：
输入：24
输出：false
示例 5：
输入：46
输出：true
提示：
1 <= N <= 10^9
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reordered-power-of-2
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from itertools import permutations


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        mis = set([str(2 ** i) for i in range(30)])
        print(mis)
        nums = []
        while n > 9:
            n, yu = divmod(n, 10)
            nums.append(str(yu))
        nums.append(str(n))
        print(nums)
        p = list(permutations(nums))
        for pn in p:
            if ''.join(pn) in mis:
                return True
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.reorderedPowerOf2(46))
    print(s.reorderedPowerOf2(1))
    print(s.reorderedPowerOf2(16777210))
