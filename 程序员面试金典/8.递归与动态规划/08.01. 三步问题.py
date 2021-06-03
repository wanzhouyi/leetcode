"""
三步问题。有个小孩正在上楼梯，楼梯有n阶台阶，小孩一次可以上1阶、2阶或3阶。
实现一种方法，计算小孩有多少种上楼梯的方式。结果可能很大，你需要对结果模1000000007。

示例1:

 输入：n = 3
 输出：4
 说明: 有四种走法
示例2:

 输入：n = 5
 输出：13
提示:

n范围在[1, 1000000]之间

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/three-steps-problem-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    """
    找到状态转移方程是关键
    f(n)=f(n-1)+f(n-2)+f(n-3)
    """

    def waysToStep(self, n: int) -> int:
        pre0 = 0
        pre1 = 0
        pre2 = 1
        for i in range(2, n + 2):
            temp = pre0 + pre1 + pre2
            pre0 = pre1 % 1000000007
            pre1 = pre2 % 1000000007
            pre2 = temp % 1000000007
        return pre2


class Solution:
    def waysToStep(self, n: int) -> int:
        a, b, c = 4, 2, 1
        if n < 3:
            return n
        if n == 3:
            return 4
        for i in range(n - 3):
            a, b, c = (a + b + c) % 1000000007, a, b
        return a


if __name__ == '__main__':
    s = Solution()
    print(s.waysToStep(3))
    print(s.waysToStep(4))
    print(s.waysToStep(5))
    print(s.waysToStep(6))
    print(s.waysToStep(1000000))
