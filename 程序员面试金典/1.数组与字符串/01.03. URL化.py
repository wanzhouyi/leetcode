"""
URL化。编写一种方法，将字符串中的空格全部替换为%20。假定该字符串尾部有足够的空间存放新增字符，并且知道字符串的“真实”长度。（注：用Java实现的话，请使用字符数组实现，以便直接在数组上操作。）
示例 1：
输入："Mr John Smith    ", 13
输出："Mr%20John%20Smith"
示例 2：
输入："               ", 5
输出："%20%20%20%20%20"
提示：

字符串长度在 [0, 500000] 范围内。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/string-to-url-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def replaceSpaces(self, S: str, length: int) -> str:
        """
        方法一：暴力法，循环替换字符然后组装
        """
        ans = []
        for i in range(length):
            char = S[i]
            if char == ' ':
                ans.append('%20')
            else:
                ans.append(char)
        return ''.join(ans)

    def replaceSpaces(self, S: str, length: int) -> str:
        """
        还是暴力解法
        """
        s1 = S.replace(' ', '%20')
        counter = 0
        idx = 0
        while counter < length:
            if s1[idx] == '%':
                idx += 3
            else:
                idx += 1
            counter += 1
        return s1[:idx]

    def replaceSpaces(self, S: str, length: int) -> str:
        return S[:length].replace(' ', '%20')


if __name__ == '__main__':
    s = Solution()
    print(s.replaceSpaces("Mr John Smith    ", 13))
    print(s.replaceSpaces("               ", 5))
