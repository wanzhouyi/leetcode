"""
给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。

示例 1：
输入：s = "1 + 1"
输出：2

示例 2：
输入：s = " 2-1 + 2 "
输出：3

示例 3：
输入：s = "(1+(4+5+2)-3)+(6+8)"
输出：23
提示：

1 <= s.length <= 3* 105
s 由数字、'+'、'-'、'('、')'、和 ' ' 组成
s 表示一个有效的表达式

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/basic-calculator
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def calculate(self, s: str) -> int:
        """
        为了方便理解,代码没有优化，使用了栈。当碰到右括号时，循环出栈直到碰到左括号。
        再看左括号的左边，如果有’+‘、’-‘运算符，则将括号内的内容结果加上符号；如果没有，则认为是正数
        最后，保留在栈中的一定没有括号，直接用sum求和即可。
        """
        s = s.replace(' ', '')  # 字符串预处理
        stack = []  # 定义栈
        curr = 0  # 指针

        def get_next_num(index):
            """
            获取以当前位置开始的数字
            """
            start = index
            while index < len(s) and s[index].isdigit():
                index += 1
            return index, int(s[start:index])

        while curr < len(s):
            if s[curr] == '(':  # 左括号直接入栈
                stack.append(s[curr])
                curr += 1
            elif s[curr] == '+' and s[curr + 1].isdigit():  # 当前是+号，下一位是数字的情况
                curr, temp = get_next_num(curr + 1)
                stack.append(temp)
            elif s[curr] == '+' and s[curr + 1] == '(':  # 当前是+号，但下一位是左括号的情况
                stack.append('+')
                stack.append('(')
                curr += 2
            elif s[curr] == '-' and s[curr + 1].isdigit():  # 当前是-号，下一位是数字的情况
                curr, temp = get_next_num(curr + 1)
                stack.append(-temp)
            elif s[curr] == '-' and s[curr + 1] == '(':  # 当前是-号，但下一位是左括号的情况
                stack.append('-')
                stack.append('(')
                curr += 2
            elif s[curr] == ')':  # 碰到右括号，则循环出栈
                temp_sum = 0
                while stack and stack[-1] != '(':
                    temp_sum += stack.pop()
                stack.pop()  # 弹出左括号’(‘
                if stack and stack[-1] == '-':  # 如果左括号左边是减号，数值取反
                    stack.pop()
                    stack.append(-temp_sum)
                elif stack and stack[-1] == '+':  # 如果左括号左边是加号，数值不变
                    stack.pop()
                    stack.append(temp_sum)
                else:  # 如果左括号左边没有符号，数值不变
                    stack.append(temp_sum)
                curr += 1
            else:  # 当前碰到的就是一个数字
                curr, num = get_next_num(curr)
                stack.append(num)
        return sum(stack)


class Solution:
    def calculate(self, s: str) -> int:
        """
        官方解法：
        由于字符串除了数字与括号外，只有加号和减号两种运算符。
        因此，如果展开表达式中所有的括号，则得到的新表达式中，数字本身不会发生变化，只是每个数字前面的符号会发生变化。
        因此，我们考虑使用一个取值为 {−1,+1} 的整数 sign 代表「当前」的符号。根据括号表达式的性质，它的取值：
        1.与字符串中当前位置的运算符有关；
        2.如果当前位置处于一系列括号之内，则也与这些括号前面的运算符有关：每当遇到一个以 -号开头的括号，
        则意味着此后的符号都要被「翻转」。
        考虑到第二点，我们需要维护一个栈 ops，其中栈顶元素记录了当前位置所处的每个括号所「共同形成」的符号。
        例如，对于字符串 1+2+(3-(4+5))：

        扫描到1+2 时，由于当前位置没有被任何括号所包含，则栈顶元素为初始值 +1；
        扫描到1+2+(3 时，当前位置被一个括号所包含，该括号前面的符号为 + 号，因此栈顶元素依然 +1；
        扫描到 1+2+(3-(4 时，当前位置被两个括号所包含，分别对应着 + 号和 - 号，由于 + 号和 -号合并的结果为 − 号，
        因此栈顶元素变为 −1。
        在得到栈 ops 之后，sign 的取值就能够确定了：如果当前遇到了 + 号，则更新 sign←ops.top()；
        如果遇到了遇到了 − 号，则更新 sign←−ops.top()。

        然后，每当遇到 ( 时，都要将当前sign 取值压入栈中；每当遇到 ) 时，都从栈中弹出一个元素。
        这样，我们能够在扫描字符串的时候，即时地更新 ops 中的元素。

        作者：LeetCode-Solution
        链接：https://leetcode-cn.com/problems/basic-calculator/solution/ji-ben-ji-suan-qi-by-leetcode-solution-jvir/
        来源：力扣（LeetCode）
        著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        """
        ops = [1]
        sign = 1

        ret = 0
        n = len(s)
        i = 0
        while i < n:
            if s[i] == ' ':
                i += 1
            elif s[i] == '+':
                sign = ops[-1]
                i += 1
            elif s[i] == '-':
                sign = -ops[-1]
                i += 1
            elif s[i] == '(':
                ops.append(sign)
                i += 1
            elif s[i] == ')':
                ops.pop()
                i += 1
            else:
                num = 0
                while i < n and s[i].isdigit():
                    num = num * 10 + ord(s[i]) - ord('0')
                    i += 1
                ret += num * sign
        return ret


if __name__ == '__main__':
    s = Solution()
    # print(s.calculate(s="1 + 1"))
    # print(s.calculate(s = " 2-1 + 2 "))
    print(s.calculate(s="(1+(4+5+2)-3)+(6+8)"))
    # print(s.calculate(s="((1+(4+5+2))-3)+(6+8)"))
