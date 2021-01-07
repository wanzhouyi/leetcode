"""
斐波那契数，通常用F(n) 表示，形成的序列称为 斐波那契数列 。该数列由0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：
F(0) = 0，F(1)= 1
F(n) = F(n - 1) + F(n - 2)，其中 n > 1
给你 n ，请计算 F(n) 。

示例 1：
输入：2
输出：1
解释：F(2) = F(1) + F(0) = 1 + 0 = 1

示例 2：
输入：3
输出：2
解释：F(3) = F(2) + F(1) = 1 + 1 = 2

示例 3：
输入：4
输出：3
解释：F(4) = F(3) + F(2) = 2 + 1 = 3

提示：
0 <= n <= 30

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/fibonacci-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    # 方法一，从上到下法，40ms
    def fib(self, n: int) -> int:
        dic = dict()
        dic[0] = 0
        dic[1] = 1

        def dfs(m):
            if m in dic.keys():
                return dic.get(m)
            ans = dfs(m - 1) + dfs(m - 2)
            dic[m] = ans
            return ans

        return dfs(n)

    # 方法二，从下往上法，32ms
    def fib(self, n: int) -> int:
        dic = dict()
        dic[0] = 0
        dic[1] = 1
        index = 2
        while 2 <= index <= n:
            dic[index] = dic[index - 1] + dic[index - 2]
            index += 1
        return dic[n]

    # 方法三，状态压缩，36ms
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        pre=0
        last=1
        index=2
        while 2 <= index <= n:
            pre,last=last,last+pre
            index+=1
        return last


if __name__ == '__main__':
    s = Solution()
    print(s.fib(2))
    print(s.fib(3))
    print(s.fib(4))
    # 注意最大边界
    print(s.fib(30))
    # 最小边界
    print(s.fib(0))
    # 次小边界
    print(s.fib(1))
