## 字典树

以下内容来源于百度百科

### 定义

又称单词查找树，Trie树，是一种树形结构，是一种哈希树的变种。  
典型应用是用于统计，排序和保存大量的字符串（但不仅限于字符串），所以经常被搜索引擎系统用于文本词频统计。  
它的优点是：利用字符串的公共前缀来减少查询时间，最大限度地减少无谓的字符串比较，查询效率比哈希树高。

### 性质

1. 根节点不包含字符，除根节点外每一个节点都只包含一个字符；
2. 从根节点到某一节点，路径上经过的字符连接起来，为该节点对应的字符串；
3. 每个节点的所有子节点包含的字符都不相同。

### 基本操作

其基本操作有：查找、插入和删除,当然删除操作比较少见。

### 应用

##### 串的快速检索

给出N个单词组成的熟词表，以及一篇全用小写英文书写的文章，请你按最早出现的顺序写出所有不在熟词表中的生词。
在这道题中，我们可以用数组枚举，用哈希，用字典树，先把熟词建一棵树，然后读入文章进行比较，这种方法效率是比较高的。

##### “串”排序

给定N个互不相同的仅由一个单词构成的英文名，让你将他们按字典序从小到大输出 用字典树进行排序，采用数组的方式创建字典树，这棵树的每个结点的所有儿子很显然地按照其字母大小排序。对这棵树进行先序遍历即可。

##### 最长公共前缀

对所有串建立字典树，对于两个串的最长公共前缀的长度即他们所在的结点的公共祖先个数，于是，问题就转化为当时公共祖先问题。

## 代码实现

```python3
class Trie:
    # 初始化
    def __init__(self):
        self.root = {}
        self.end = "#"
 
    # 添加单词
    def add(self, word: str):
        node = self.root
        for char in word:
            node = node.setdefault(char, {})
        node[self.end] = None
 
    # 搜索单词是否存在
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return self.end in node
```

```python3
# -*- coding:utf-8 -*-
"""
Description:大变双向字典树
迭代次数默认最大999，可以增加但是没必要。其实能深到999层，那这个序列还是选择另外的处理方式吧。

@author: WangLeAi
@date: 2018/8/15
"""


class TrieNode(object):
    def __init__(self, value=None, count=0, parent=None):
        # 值
        self.value = value
        # 频数统计
        self.count = count
        # 父结点
        self.parent = parent
        # 子节点，{value:TrieNode}
        self.children = {}


class Trie(object):
    def __init__(self):
        # 创建空的根节点
        self.root = TrieNode()

    def insert(self, sequence):
        """
        基操，插入一个序列
        :param sequence: 列表
        :return:
        """
        cur_node = self.root
        for item in sequence:
            if item not in cur_node.children:
                # 插入结点
                child = TrieNode(value=item, count=1, parent=cur_node)
                cur_node.children[item] = child
                cur_node = child
            else:
                # 更新结点
                cur_node = cur_node.children[item]
                cur_node.count += 1

    def search(self, sequence):
        """
        基操，查询是否存在完整序列
        :param sequence: 列表
        :return:
        """
        cur_node = self.root
        mark = True
        for item in sequence:
            if item not in cur_node.children:
                mark = False
                break
            else:
                cur_node = cur_node.children[item]
        # 如果还有子结点，说明序列并非完整
        if cur_node.children:
            mark = False
        return mark

    def delete(self, sequence):
        """
        基操，删除序列，准确来说是减少计数
        :param sequence: 列表
        :return:
        """
        mark = False
        if self.search(sequence):
            mark = True
            cur_node = self.root
            for item in sequence:
                cur_node.children[item].count -= 1
                if cur_node.children[item].count == 0:
                    cur_node.children.pop(item)
                    break
                else:
                    cur_node = cur_node.children[item]
        return mark

    def search_part(self, sequence, prefix, suffix, start_node=None):
        """
        递归查找子序列，返回前缀和后缀结点
        此处简化操作，仅返回一位前后缀的内容与频数
        :param sequence: 列表
        :param prefix: 前缀字典，初始传入空字典
        :param suffix: 后缀字典，初始传入空字典
        :param start_node: 起始结点，用于子树的查询
        :return:
        """
        if start_node:
            cur_node = start_node
            prefix_node = start_node.parent
        else:
            cur_node = self.root
            prefix_node = self.root
        mark = True
        # 必须从第一个结点开始对比
        for i in range(len(sequence)):
            if i == 0:
                if sequence[i] != cur_node.value:
                    for child_node in cur_node.children.values():
                        self.search_part(sequence, prefix, suffix, child_node)
                    mark = False
                    break
            else:
                if sequence[i] not in cur_node.children:
                    for child_node in cur_node.children.values():
                        self.search_part(sequence, prefix, suffix, child_node)
                    mark = False
                    break
                else:
                    cur_node = cur_node.children[sequence[i]]
        if mark:
            if prefix_node.value:
                # 前缀数量取序列词中最后一词的频数
                if prefix_node.value in prefix:
                    prefix[prefix_node.value] += cur_node.count
                else:
                    prefix[prefix_node.value] = cur_node.count
            for suffix_node in cur_node.children.values():
                if suffix_node.value in suffix:
                    suffix[suffix_node.value] += suffix_node.count
                else:
                    suffix[suffix_node.value] = suffix_node.count
            # 即使找到一部分还需继续查找子结点
            for child_node in cur_node.children.values():
                self.search_part(sequence, prefix, suffix, child_node)


if __name__ == "__main__":
    trie = Trie()
    texts = [["葬爱", "少年", "葬爱", "少年", "慕周力", "哈哈"], ["葬爱", "少年", "阿西吧"], ["烈", "烈", "风", "中"], ["忘记", "了", "爱"],
             ["埋葬", "了", "爱"]]
    for text in texts:
        trie.insert(text)
    markx = trie.search(["忘记", "了", "爱"])
    print(markx)
    markx = trie.search(["忘记", "了"])
    print(markx)
    markx = trie.search(["忘记", "爱"])
    print(markx)
    markx = trie.delete(["葬爱", "少年", "王周力"])
    print(markx)
    prefixx = {}
    suffixx = {}
    trie.search_part(["葬爱", "少年"], prefixx, suffixx)
    print(prefixx)
    print(suffixx)


```