"""
给定一个含有数字和运算符的字符串，为表达式添加括号，改变其运算优先级以求出不同的结果。
你需要给出所有可能的组合的结果。有效的运算符号包含 +,-以及*。

示例1:
输入: "2-1-1"
输出: [0, 2]
解释: 
((2-1)-1) = 0 
(2-(1-1)) = 2

示例2:
输入: "2*3-4*5"
输出: [-34, -14, -10, -10, 10]
解释: 
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/different-ways-to-add-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    # 方法一，分治，44ms，59%
    def diffWaysToCompute(self, input: str) -> List[int]:
        # 如果只有数字，直接返回
        if input.isdigit():
            return [int(input)]
        res = []
        for idx, char in enumerate(input):
            if char in ['+', '-', '*']:
                # 1.分解：遇到运算符，计算左右两侧的结果集
                # 2.解决：diffWaysToCompute 递归函数求出子问题的解
                left = self.diffWaysToCompute(input[:idx])
                right = self.diffWaysToCompute(input[idx + 1:])
                # 3.合并：根据运算符合并子问题的解
                for l in left:
                    for r in right:
                        if char == '+':
                            res.append(l + r)
                        elif char == '-':
                            res.append(l - r)
                        elif char == '*':
                            res.append(l * r)
        return res

    # 方法一，分治+剪枝，56ms，15.6%
    def diffWaysToCompute(self, input: str) -> List[int]:
        memo = {}

        def cal(lo, hi):
            if input[lo:hi].isdigit():
                return [int(input[lo:hi])]
            if (lo, hi) in memo:
                return memo[(lo, hi)]
            ret = []
            for idx, char in enumerate(input[lo:hi]):
                if char in ['+', '-', '*']:
                    left = cal(lo, lo + idx)
                    right = cal(lo + idx + 1, hi)
                    ret.extend([eval(str(i) + char + str(j)) for i in left for j in right])
                    memo[(lo, hi)] = ret
            return ret

        return cal(0, len(input))


if __name__ == '__main__':
    s = Solution()
    print(s.diffWaysToCompute("2-1-1"))
