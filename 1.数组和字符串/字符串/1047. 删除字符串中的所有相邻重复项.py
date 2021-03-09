"""
给出由小写字母组成的字符串S，重复项删除操作会选择两个相邻且相同的字母，并删除它们。

在 S 上反复执行重复项删除操作，直到无法继续删除。

在完成所有重复项删除操作后返回最终的字符串。答案保证唯一。

示例：

输入："abbaca"
输出："ca"
解释：
例如，在 "abbaca" 中，我们可以删除 "bb" 由于两字母相邻且相同，这是此时唯一可以执行删除操作的重复项。之后我们得到字符串 "aaca"，其中又只有 "aa" 可以执行重复项删除操作，所以最后的字符串为 "ca"。

提示：

1 <= S.length <= 20000
S 仅由小写英文字母组成。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-all-adjacent-duplicates-in-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def removeDuplicates(self, S: str) -> str:
        """
        模拟题意，反复比较当前字符和下一个字符是否相等
        如'abbc'，当curr=1时，和index=2的字符相等，应消掉索引为1和2的字符。此时，curr应回退到0，即curr=curr-1
        特殊地，如‘aabc'，当curr=0时，如果和index=1的字符相等，消掉索引为0和1的字符后，curr仍为0
        """
        curr = 0
        while curr < len(S) - 1:
            if S[curr] == S[curr + 1]:
                S = S[:curr] + S[curr + 2:]
                curr = 0 if curr == 0 else curr - 1
            else:
                curr += 1
        return S

    def removeDuplicates(self, S: str) -> str:
        """
        利用栈的原理，如果栈顶字符和当前待入栈字符相等，则不入栈且弹出栈顶元素
        """
        stack = []
        for char in S:
            if stack and char == stack[-1]:
                stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)


if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates("abbaca"))
    print(s.removeDuplicates("aabcccc"))
