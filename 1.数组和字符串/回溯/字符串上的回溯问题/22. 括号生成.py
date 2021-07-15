"""
数字 n代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

示例 1：
输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]
示例 2：
输入：n = 1
输出：["()"]

提示：
1 <= n <= 8

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/generate-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def is_valid_group(arr):
            stack = []
            while arr:
                char = arr.pop(0)
                if char == '(':
                    stack.append(char)
                else:
                    if stack and stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
            if not stack:
                return True
            else:
                return False

        ans = []
        left, right = ['('] * n, [')'] * n

        def back_track(path: list):
            if not left and not right:
                if is_valid_group(path[:]):
                    ans.append(''.join(path))
                return
            if left:
                left.pop()
                path.append('(')
                back_track(path)
                path.pop()
                left.append('(')

            if right:
                right.pop()
                path.append(')')
                back_track(path)
                path.pop()
                right.append(')')

        back_track([])
        return ans


# ------官解
class Solution:
    """
    方法一：暴力法
    思路

    我们可以生成所有 2^2n个 '(' 和 ')' 字符构成的序列，然后我们检查每一个是否有效即可。
    算法
    为了生成所有序列，我们可以使用递归。长度为 n 的序列就是在长度为 n-1 的序列前加一个 '(' 或 ')'。

    为了检查序列是否有效，我们遍历这个序列，并使用一个变量 balance 表示左括号的数量减去右括号的数量。
    如果在遍历过程中 balance 的值小于零，或者结束时 balance 的值不为零，那么该序列就是无效的，否则它是有效的。

    作者：LeetCode-Solution
    链接：https://leetcode-cn.com/problems/generate-parentheses/solution/gua-hao-sheng-cheng-by-leetcode-solution/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def generateParenthesis(self, n: int) -> List[str]:
        def generate(A):
            if len(A) == 2 * n:
                if valid(A):
                    ans.append("".join(A))
            else:
                A.append('(')
                generate(A)
                A.pop()
                A.append(')')
                generate(A)
                A.pop()

        def valid(A):
            bal = 0
            for c in A:
                if c == '(':
                    bal += 1
                else:
                    bal -= 1
                if bal < 0: return False
            return bal == 0

        ans = []
        generate([])
        return ans


class Solution:
    """
    方法二：回溯法
    思路和算法

    方法一还有改进的余地：我们可以只在序列仍然保持有效时才添加 '(' or ')'，而不是像 方法一 那样每次添加。
    我们可以通过跟踪到目前为止放置的左括号和右括号的数目来做到这一点，

    如果左括号数量不大于 n，我们可以放一个左括号。如果右括号数量小于左括号的数量，我们可以放一个右括号。

    作者：LeetCode-Solution
    链接：https://leetcode-cn.com/problems/generate-parentheses/solution/gua-hao-sheng-cheng-by-leetcode-solution/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(S, left, right):
            if len(S) == 2 * n:
                ans.append(''.join(S))
                return
            if left < n:
                S.append('(')
                backtrack(S, left + 1, right)
                S.pop()
            if right < left:
                S.append(')')
                backtrack(S, left, right + 1)
                S.pop()

        backtrack([], 0, 0)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(3))
    print(s.generateParenthesis(1))
    print(s.generateParenthesis(8))
