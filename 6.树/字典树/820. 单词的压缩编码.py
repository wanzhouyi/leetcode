"""
单词数组words 的 有效编码 由任意助记字符串 s 和下标数组 indices 组成，且满足：

words.length == indices.length
助记字符串 s 以 '#' 字符结尾
对于每个下标 indices[i] ，s 的一个从 indices[i] 开始、到下一个 '#' 字符结束（但不包括 '#'）的 子字符串 恰好与 words[i] 相等
给你一个单词数组words ，返回成功对 words 进行编码的最小助记字符串 s 的长度 。



示例 1：

输入：words = ["time", "me", "bell"]
输出：10
解释：一组有效编码为 s = "time#bell#" 和 indices = [0, 2, 5] 。
words[0] = "time" ，s 开始于 indices[0] = 0 到下一个 '#' 结束的子字符串，如加粗部分所示 "time#bell#"
words[1] = "me" ，s 开始于 indices[1] = 2 到下一个 '#' 结束的子字符串，如加粗部分所示 "time#bell#"
words[2] = "bell" ，s 开始于 indices[2] = 5 到下一个 '#' 结束的子字符串，如加粗部分所示 "time#bell#"
示例 2：

输入：words = ["t"]
输出：2
解释：一组有效编码为 s = "t#" 和 indices = [0] 。


提示：

1 <= words.length <= 2000
1 <= words[i].length <= 7
words[i] 仅由小写字母组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/short-encoding-of-words
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
from functools import reduce
from typing import List


class Solution:
    def __init__(self):
        self.trie = {}
        # self.end = '#'
        self.counter = 0

    def insert_word(self, word):
        node = self.trie
        for char in word[::-1]:
            node.setdefault(char, {})
            node = node[char]
        # node[self.end] = None

    def dfs(self, node, cnt):
        if not node:
            self.counter += (cnt + 1)
            return
        for char in node:
            self.dfs(node[char], cnt + 1)

    def minimumLengthEncoding(self, words: List[str]) -> int:
        for word in words:
            self.insert_word(word)

        print(self.trie)

        self.dfs(self.trie, 0)
        return self.counter


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = list(set(words))  # remove duplicates
        # Trie is a nested dictionary with nodes created
        # when fetched entries are missing
        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()

        # reduce(..., S, trie) is trie[S[0]][S[1]][S[2]][...][S[S.length - 1]]
        nodes = [reduce(dict.__getitem__, word[::-1], trie)
                 for word in words]

        # Add word to the answer if it's node has no neighbors
        return sum(len(word) + 1
                   for i, word in enumerate(words)
                   if len(nodes[i]) == 0)


if __name__ == '__main__':
    s = Solution()
    print(s.minimumLengthEncoding(words=["time", "me", "bell", 'gome']))
