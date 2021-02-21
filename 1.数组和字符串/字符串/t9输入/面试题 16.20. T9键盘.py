"""
在老式手机上，用户通过数字键盘输入，手机将提供与这些数字相匹配的单词列表。每个数字映射到0至4个字母。给定一个数字序列，实现一个算法来返回匹配单词的列表。你会得到一张含有有效单词的列表。映射如下图所示：
示例 1:

输入: num = "8733", words = ["tree", "used"]
输出: ["tree", "used"]
示例 2:

输入: num = "2", words = ["a", "b", "c", "d"]
输出: ["a", "b", "c"]
提示：

num.length <= 1000
words.length <= 500
words[i].length == num.length
num中不会出现 0, 1 这两个数字

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/t9-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def getValidT9Words(self, num: str, words: List[str]) -> List[str]:
        t9 = '22233344455566677778889999'  # 对应a-z

        def letter_digit(x):
            assert 'a' <= x <= 'z'
            return t9[ord(x) - 97]

        def word_code(word):
            return ''.join(map(letter_digit, word))

        word_digit = []
        for word in words:
            word_digit.append(word_code(word))

        return [words[i] for i, wc in enumerate(word_digit) if wc == num]

    def getValidT9Words(self, num: str, words: List[str]) -> List[str]:
        dic = {
            '1': '!@#',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
            '0': ' '
        }
        candidate = words
        numList = list(num)
        for i, n in enumerate(numList):
            candidate = [w for w in candidate if w[i] in dic[n]]
        return candidate


if __name__ == '__main__':
    s = Solution()
    print(s.getValidT9Words(num="8733", words=["tree", "used"]))
