"""
给定两个字符串形式的非负整数num1 和num2，计算它们的和。
提示：

num1 和num2的长度都小于 5100
num1 和num2 都只包含数字0-9
num1 和num2 都不包含任何前导零
你不能使用任何內建 BigInteger 库，也不能直接将输入的字符串转换为整数形式

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ls1, ls2 = list(num1), list(num2)
        ans = []
        jinwei = 0
        while ls1 and ls2:
            a, b = ls1.pop(), ls2.pop()
            temp = int(a) + int(b) + jinwei
            if temp > 9:
                ans.append(temp - 10)
                jinwei = 1
            else:
                ans.append(temp)
                jinwei = 0
        while ls1:
            temp = int(ls1.pop()) + jinwei
            if temp > 9:
                ans.append(temp - 10)
                jinwei = 1
            else:
                ans.append(temp)
                jinwei = 0

        while ls2:
            temp = int(ls2.pop()) + jinwei
            if temp > 9:
                ans.append(temp - 10)
                jinwei = 1
            else:
                ans.append(temp)
                jinwei = 0
        if jinwei > 0:
            ans.append(jinwei)

        return ''.join(map(str, ans[::-1]))


if __name__ == '__main__':
    s = Solution()
    print(s.addStrings('123456789', '987643164987'))
