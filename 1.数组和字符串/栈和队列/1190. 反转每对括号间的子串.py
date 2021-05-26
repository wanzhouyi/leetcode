"""
给出一个字符串s（仅含有小写英文字母和括号）。

请你按照从括号内到外的顺序，逐层反转每对匹配括号中的字符串，并返回最终的结果。

注意，您的结果中 不应 包含任何括号。



示例 1：

输入：s = "(abcd)"
输出："dcba"
示例 2：

输入：s = "(u(love)i)"
输出："iloveu"
示例 3：

输入：s = "(ed(et(oc))el)"
输出："leetcode"
示例 4：

输入：s = "a(bcdefghijkl(mno)p)q"
输出："apmnolkjihgfedcbq"


提示：

0 <= s.length <= 2000
s 中只有小写英文字母和括号
我们确保所有括号都是成对出现的

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-substrings-between-each-pair-of-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for char in s:
            if char != ')':
                stack.append(char)
            else:
                temp_stack = []
                while stack:
                    temp_s = stack.pop()
                    if temp_s != '(':
                        temp_stack.append(temp_s)
                    else:
                        stack.extend(temp_stack)
                        break
        return ''.join(stack)


if __name__ == '__main__':
    s = Solution()
    print(s.reverseParentheses(s="(abcd)"))  # "dcba"
    print(s.reverseParentheses(s="(u(love)i)"))  # iloveu
    print(s.reverseParentheses(s="(ed(et(oc))el)"))  # leetcode
    print(s.reverseParentheses('a(bcdefghijkl(mno)p)q'))  # apmnolkjihgfedcbq
    print(s.reverseParentheses('()'))
    print(s.reverseParentheses(''))
