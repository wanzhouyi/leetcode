"""
在英语中，我们有一个叫做词根(root)的概念，它可以跟着其他一些词组成另一个较长的单词——我们称这个词为继承词(successor)。
例如，词根an，跟随着单词other(其他)，可以形成新的单词another(另一个)。
现在，给定一个由许多词根组成的词典和一个句子。你需要将句子中的所有继承词用词根替换掉。
如果继承词有许多可以形成它的词根，则用最短的词根替换它。
你需要输出替换之后的句子。

示例 1：
输入：dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
输出："the cat was rat by the bat"
示例 2：
输入：dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
输出："a a b c"
示例 3：
输入：dictionary = ["a", "aa", "aaa", "aaaa"], sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"
输出："a a a a a a a a bbb baba a"
示例 4：
输入：dictionary = ["catt","cat","bat","rat"], sentence = "the cattle was rattled by the battery"
输出："the cat was rat by the bat"
示例 5：
输入：dictionary = ["ac","ab"], sentence = "it is abnormal that this solution is accepted"
输出："it is ab that this solution is ac"

提示：

1 <= dictionary.length<= 1000
1 <= dictionary[i].length <= 100
dictionary[i]仅由小写字母组成。
1 <= sentence.length <= 10^6
sentence仅由小写字母和空格组成。
sentence 中单词的总量在范围 [1, 1000] 内。
sentence 中每个单词的长度在范围 [1, 1000] 内。
sentence 中单词之间由一个空格隔开。
sentence没有前导或尾随空格。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/replace-words
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
from functools import reduce
from typing import List


class Trie:
    def __init__(self):
        self.trie = {}
        self.end = '#'

    def insert(self, word):
        node = self.trie
        for char in word:
            node.setdefault(char, {})
            node = node[char]
        node[self.end] = None

    def search_prefix(self, word):
        node = self.trie
        for idx, char in enumerate(word):
            if char in node:
                node = node[char]
                if self.end in node:
                    return word[:idx + 1]
            else:
                break
        return word


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        tr = Trie()
        for di in dictionary:
            tr.insert(di)
        print(tr.trie)
        ans = []
        for word in sentence.split(' '):
            ans.append(tr.search_prefix(word))
        return ' '.join(ans)


# 官方题解
class Solution:
    def replaceWords(self, dictionary, sentence):
        """
        方法一：前缀哈希【通过】
        思路
        遍历句子中每个单词，查看单词前缀是否为词根。
        算法
        将所有词根 roots 存储到集合 Set 中。遍历所有单词，判断其前缀是否为词根。
        如果是，则使用前缀代替该单词；否则不改变该单词。

        作者：LeetCode
        链接：https://leetcode-cn.com/problems/replace-words/solution/dan-ci-ti-huan-by-leetcode/
        来源：力扣（LeetCode）
        著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        """
        rootset = set(dictionary)

        def replace(word):
            for i in range(1, len(word)):
                if word[:i] in rootset:
                    return word[:i]
            return word

        return " ".join(map(replace, sentence.split()))


class Solution(object):
    """
    方法二：前缀树【通过】
    思路和算法

    把所有的词根放入前缀树中，在树上查找每个单词的最短词根，该操作可在线性时间内完成。
    """

    def replaceWords(self, roots, sentence):
        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()
        END = True

        for root in roots:
            reduce(dict.__getitem__, root, trie)[END] = root

        def replace(word):
            cur = trie
            for letter in word:
                if letter not in cur or END in cur: break
                cur = cur[letter]
            return cur.get(END, word)

        return " ".join(map(replace, sentence.split()))


if __name__ == '__main__':
    s = Solution()
    print(s.replaceWords(dictionary=["cat", "bat", "rat"],
                         sentence="the cattle was rattled by the battery"))
    print(s.replaceWords(dictionary=["a", "b", "c"], sentence="aadsfasf absbs bbab cadsfafs"))
    print(s.replaceWords(dictionary=["a", "aa", "aaa", "aaaa"],
                         sentence="a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"))
    print(s.replaceWords(dictionary=["catt", "cat", "bat", "rat"],
                         sentence="the cattle was rattled by the battery"))
    print(s.replaceWords(dictionary=["ac", "ab"],
                         sentence="it is abnormal that this solution is accepted"))
