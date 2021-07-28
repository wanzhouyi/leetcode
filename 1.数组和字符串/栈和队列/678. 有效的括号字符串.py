"""
给定一个只包含三种字符的字符串：（，）和 *，写一个函数来检验这个字符串是否为有效字符串。有效字符串具有如下规则：

任何左括号 (必须有相应的右括号 )。
任何右括号 )必须有相应的左括号 (。
左括号 ( 必须在对应的右括号之前 )。
*可以被视为单个右括号 )，或单个左括号 (，或一个空字符串。
一个空字符串也被视为有效字符串。
示例 1:

输入: "()"
输出: True
示例 2:

输入: "(*)"
输出: True
示例 3:

输入: "(*))"
输出: True
注意:

字符串大小将在 [1，100] 范围内。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-parenthesis-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    """
    定义两个栈，leftStack 存 ' ( ' 所在位置的下标，starStack 存 '*' 所在位置的下标。

    1.当遇到 ' ( ' 时，' ( ' 所在位置的下标入栈；当遇到 ' * ' 时，' * ' 所在位置的下标入栈。

    2.当遇到 ' ) ' 时，要令 leftStack 中的栈顶元素出栈，若此时 leftStack 为空，则继续看 starStack 是否为空，若不为空则 starStack 栈顶元素出栈，若为空返回则 false (遇到了 ' ) '，但在这之前一个 ' ( ' 和 ' * ' 都没遇到，则一定不会匹配)。

    3.当字符串全部遍历完时，若 starStack 的长度比 leftStack 的长度要小，则返回 false (有剩余的 ' ( '，但 ' * ' 的数量不够了，则一定不会匹配)；否则，比较两个栈的栈顶元素值的大小，要保证 ' ( ' 在 ' * ' 的左边(starStack.peek() > leftStack.peek())才能匹配成功，当遇到满足条件的栈顶元素时，栈顶元素出栈，继续比较下一个。只要有一次该条件不满足，则直接返回 false；否则，返回 true。

    作者：Booooo_
    链接：https://leetcode-cn.com/problems/valid-parenthesis-string/solution/you-xiao-de-gua-hao-zi-fu-chuan-zhan-lia-w0n2/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def checkValidString(self, s: str) -> bool:
        stack_left = []
        stack_star = []
        for idx, char in enumerate(s):
            if char == '(':
                stack_left.append(idx)
            elif char == '*':
                stack_star.append(idx)
            elif char == ')':
                if stack_left:
                    stack_left.pop()
                elif stack_star:
                    stack_star.pop()
                else:
                    return False
        while stack_left and stack_star and stack_left[-1] < stack_star[-1]:
            stack_left.pop()
            stack_star.pop()
        if stack_left:
            return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.checkValidString("(*))"))
