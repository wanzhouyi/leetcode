"""
实现一个 MapSum 类，支持两个方法，insert和sum：

MapSum() 初始化 MapSum 对象
void insert(String key, int val) 插入 key-val 键值对，字符串表示键 key ，整数表示值 val 。如果键 key 已经存在，那么原来的键值对将被替代成新的键值对。
int sum(string prefix) 返回所有以该前缀 prefix 开头的键 key 的值的总和。

示例：
输入：
["MapSum", "insert", "sum", "insert", "sum"]
[[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]
输出：
[null, null, 3, null, 5]

解释：
MapSum mapSum = new MapSum();
mapSum.insert("apple", 3);  
mapSum.sum("ap");           // return 3 (apple = 3)
mapSum.insert("app", 2);    
mapSum.sum("ap");           // return 5 (apple + app = 3 + 2 = 5)

提示：
1 <= key.length, prefix.length <= 50
key 和 prefix 仅由小写英文字母组成
1 <= val <= 1000
最多调用 50 次 insert 和 sum

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/map-sum-pairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Trie:
    def __init__(self):
        self.root = {}
        self.end = '#'

    def add_or_update(self, key, val):
        node = self.root
        for char in key:
            node = node.setdefault(char, {})
        node[self.end] = val

    def search(self, word):
        node = self.root
        for char in word:
            if char in node:
                node = node[char]
            else:
                return 0

        ans = 0
        stack = [node]
        while stack:
            temp_node = stack.pop(0)
            if self.end in temp_node:
                ans += temp_node[self.end]

            for n in temp_node.keys():
                if n != self.end:
                    stack.append(temp_node[n])
        return ans


class MapSum:

    def __init__(self):
        self.trie = Trie()

    def insert(self, key: str, val: int) -> None:
        self.trie.add_or_update(key, val)
        # return self.trie

    def sum(self, prefix: str) -> int:
        return self.trie.search(prefix)


# 官解
'''
方法一：暴力扫描
思路与算法

我们将所有的 key-val 键值进行存储，每次需要搜索给定的前缀 prefix 时，我们依次搜索所有的键值。
如果键值包含给定的前缀，则我们将其 val 进行相加，返回所有符合要求的 val 的和。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/map-sum-pairs/solution/jian-zhi-ying-she-by-leetcode-solution-j4xy/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。'''


class MapSum:
    def __init__(self):
        self.map = {}

    def insert(self, key: str, val: int) -> None:
        self.map[key] = val

    def sum(self, prefix: str) -> int:
        res = 0
        for key, val in self.map.items():
            if key.startswith(prefix):
                res += val
        return res


'''
方法二：前缀哈希映射
思路与算法

我们可以用哈希表存储所有可能前缀的值。
当我们得到一个新的 key-val 键值，我们将 key 的每个前缀 prefix[i] 都在哈希表中进行存储，
我们需要更新每个前缀prefix[i] 对应的值。
我们计算出它对应的值的增加为 delta，计算方式如下：

如果键 key 不存在，则此时 delta 等于val。
如果键 key 存在，则此时键key 对应得前缀的值都增加 val−map[key]，其中 map[key] 表示键key 当前对应的值。
我们在完成前缀的值改写后，同时要更新键key 对应的值为val。
求sum 时,我们直接利用哈希表查找给定的前缀对应的值即可。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/map-sum-pairs/solution/jian-zhi-ying-she-by-leetcode-solution-j4xy/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。'''


class MapSum:
    def __init__(self):
        self.map = {}
        self.prefixmap = {}

    def insert(self, key: str, val: int) -> None:
        delta = val
        if key in self.map:
            delta -= self.map[key]
        self.map[key] = val
        for i in range(len(key)):
            currprefix = key[0:i + 1]
            if currprefix in self.prefixmap:
                self.prefixmap[currprefix] += delta
            else:
                self.prefixmap[currprefix] = delta

    def sum(self, prefix: str) -> int:
        if prefix in self.prefixmap:
            return self.prefixmap[prefix]
        else:
            return 0


'''
方法三：字典树
思路与算法

由于我们要处理前缀，自然而然联想到可以用 Trie（前缀树）来处理此问题。
处理方法跟方法二的原理一样，我们直接在前缀对应的 Trie 的每个节点存储该前缀对应的值。

insert 操作：原理与方法二一样，我们首先求出前缀对应的值的改变delta，我们直接在Trie 节点上更新键 key 的每个前缀对应的值。
sum 操作: 我们直接在前缀树上搜索该给定的前缀对应的值即可，如果给定的前缀不在前缀树中，则返回 0。
当然在实际中我们也可以在Trie 的节点只存储键key 对应的val, 每次求sum 时利用DFS 或BFS 遍历前缀树的子树即可。
'''


class TrieNode:
    def __init__(self):
        self.val = 0
        self.next = [None for _ in range(26)]


class MapSum:
    def __init__(self):
        self.root = TrieNode()
        self.map = {}

    def insert(self, key: str, val: int) -> None:
        delta = val
        if key in self.map:
            delta -= self.map[key]
        self.map[key] = val
        node = self.root
        for c in key:
            if node.next[ord(c) - ord('a')] is None:
                node.next[ord(c) - ord('a')] = TrieNode()
            node = node.next[ord(c) - ord('a')]
            node.val += delta

    def sum(self, prefix: str) -> int:
        node = self.root
        for c in prefix:
            if node.next[ord(c) - ord('a')] is None:
                return 0
            node = node.next[ord(c) - ord('a')]
        return node.val


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
if __name__ == '__main__':
    # s = MapSum()
    # s.insert('app', 3)
    # s.insert('app', 5)
    # s.insert('apppie', 9)
    # s.insert('apple', 8)
    # print(s.sum('app'))

    mapSum = MapSum()
    mapSum.insert("apple", 3)
    print(mapSum.sum("ap"))  # return 3(apple=3)
    mapSum.insert("app", 2)
    print(mapSum.sum("ap"))  # return 5(apple + app = 3 + 2 = 5)
