"""
请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

示例 1：
输入：s = "We are happy."
输出："We%20are%20happy."

限制：
0 <= s 的长度 <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    # 方法一，系统函数，36ms
    def replaceSpace(self, s: str) -> str:
        return s.replace(' ', '%20')

    # 方法二，分割法，32ms
    def replaceSpace(self, s: str) -> str:
        return '%20'.join(s.split(' '))

    # 方法三，遍历法，32ms
    def replaceSpace(self, s: str) -> str:
        result=[]
        for char in s:
            result.append('%20' if char==' ' else char)
        return ''.join(result)



if __name__ == '__main__':
    s = Solution()
    print(s.replaceSpace("We are happy."))
