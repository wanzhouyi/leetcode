"""
实现一个 Trie (前缀树)，包含insert,search, 和startsWith这三个操作。
示例:
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // 返回 true
trie.search("app");     // 返回 false
trie.startsWith("app"); // 返回 true
trie.insert("app");   
trie.search("app");     // 返回 true
说明:

你可以假设所有的输入都是由小写字母a-z构成的。
保证所有输入均为非空字符串。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/implement-trie-prefix-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}
        self.end = '#'

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.trie
        for char in word:
            node = node.setdefault(char, {})
        node[self.end] = None

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.trie
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return self.end in node

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.trie
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True


if __name__ == '__main__':
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))  # 返回    true
    print(trie.search("app"))  # 返回    false
    print(trie.startsWith("app"))  # 返回   true
    trie.insert("app")
    print(trie.search("app"))  # 返回    true
