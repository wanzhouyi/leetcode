"""
给定一个化学式formula（作为字符串），返回每种原子的数量。
原子总是以一个大写字母开始，接着跟随0个或任意个小写字母，表示原子的名字。
如果数量大于 1，原子后会跟着数字表示原子的数量。如果数量等于 1 则不会跟数字。例如，H2O 和 H2O2 是可行的，但 H1O2 这个表达是不可行的。
两个化学式连在一起是新的化学式。例如H2O2He3Mg4 也是化学式。
一个括号中的化学式和数字（可选择性添加）也是化学式。例如 (H2O2) 和 (H2O2)3 是化学式。
给定一个化学式formula ，返回所有原子的数量。格式为：第一个（按字典序）原子的名字，跟着它的数量（如果数量大于 1），然后是第二个原子的名字（按字典序），跟着它的数量（如果数量大于 1），以此类推。

示例 1：
输入：formula = "H2O"
输出："H2O"
解释：
原子的数量是 {'H': 2, 'O': 1}。

示例 2：
输入：formula = "Mg(OH)2"
输出："H2MgO2"
解释： 
原子的数量是 {'H': 2, 'Mg': 1, 'O': 2}。

示例 3：
输入：formula = "K4(ON(SO3)2)2"
输出："K4N2O14S4"
解释：
原子的数量是 {'K': 4, 'N': 2, 'O': 14, 'S': 4}。

示例 4：
输入：formula = "Be32"
输出："Be32"

提示：

1 <= formula.length<= 1000
formula 由小写英文字母、数字 '(' 和 ')' 组成。
formula 是有效的化学式。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-atoms
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = []
        ls = list(formula)
        while ls:
            char = ls.pop(0)
            if char == ')':
                temp_chars = []
                while stack:
                    temp = stack.pop()
                    if temp == '(':
                        break
                    else:
                        temp_chars.append(temp)
                dic_ans = self.cal_in_bracket(''.join(temp_chars[::-1]))
                multi_num = None
                while ls:
                    c = ls.pop(0)
                    if c.isdigit():
                        if not multi_num:
                            multi_num = int(c)
                        else:
                            multi_num = multi_num * 10 + int(c)
                    else:
                        ls.insert(0, c)
                        break

                if not multi_num:
                    multi_num = 1

                for key in dic_ans.keys():
                    stack.append(key)
                    stack.append(str(dic_ans[key] * multi_num))

            else:
                stack.append(char)

        # print(ls)
        # print(stack)
        ans = self.cal_in_bracket(''.join(stack))
        keys = sorted(ans.keys())
        res = ''
        for key in keys:
            res = res + key + ('' if ans[key] == 1 else str(ans[key]))
        return res

    def cal_in_bracket(self, formula):
        ans = dict()
        last = None
        last_num = None
        for char in formula:
            if char.isupper():  # 大写字母
                if last:  # last不为空
                    atom = last
                    if not last_num:
                        last_num = 1
                    if ans.get(atom):
                        ans[atom] += last_num
                    else:
                        ans[atom] = last_num
                    last_num = None
                    last = char
                else:  # last为空
                    last = char
            elif char.islower():  # 小写字母
                last = last + char
            elif char.isdigit():  # 数字
                if last_num:  # 有数了
                    last_num = last_num * 10 + int(char)
                else:  # 还没数
                    last_num = int(char)
        if not last_num:
            last_num = 1
        if ans.get(last):
            ans[last] += last_num
        else:
            ans[last] = last_num

        return ans
