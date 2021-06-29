"""
请实现两个函数，分别用来序列化和反序列化二叉树。

你需要设计一个算法来实现二叉树的序列化与反序列化。
这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。

提示：输入输出格式与 LeetCode 目前使用的方式一致，详情请参阅LeetCode 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。



示例：


输入：root = [1,2,3,null,null,4,5]
输出：[1,2,3,null,null,4,5]


注意：本题与主站 297 题相同：https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/xu-lie-hua-er-cha-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for a binary tree node.
import collections


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import deque


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        ans = []
        stack = deque([root])
        while stack:
            node = stack.popleft()
            if not node:
                ans.append('#')
            else:
                ans.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        return ans

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        root = None
        if not data:
            return root
        else:
            root = TreeNode(data[0])
        stack = deque([root])
        for i in range(1, len(data), 2):
            parent = stack.popleft()
            if not parent:
                continue

            if data[i] == '#':
                node = None
            else:
                node = TreeNode(data[i])
                parent.left = node
                stack.append(node)

            if i + 1 < len(data):
                if data[i + 1] == '#':
                    node = None
                else:
                    node = TreeNode(data[i + 1])
                    parent.right = node
                    stack.append(node)
        return root


class Codec:
    """
    解题思路：
    通常使用的前序、中序、后序、层序遍历记录的二叉树的信息不完整，即唯一的输出序列可能对应着多种二叉树可能性。
    题目要求的 序列化 和 反序列化 是 可逆操作 。因此，序列化的字符串应携带 完整的二叉树信息 。

    观察题目示例，序列化的字符串实际上是二叉树的 “层序遍历”（BFS）结果，本文也采用层序遍历。

    为完整表示二叉树，考虑将叶节点下的 null 也记录。
    在此基础上，对于列表中任意某节点 node ，其左子节点 node.left 和右子节点 node.right 在序列中的位置都是 唯一确定 的。如下图所示：

    上图规律可总结为下表：
    node.val node的索引 node.left的索引 node.right的索引
    11	        00	        11	        22
    22	        11	        33	        44
    33	        22	        55	        66
    44	        55	        77	        88
    55	        66	        99	        1010
    设 m 为列表区间[0,n] 中的 null 节点个数，则可总结出根节点、左子节点、右子节点的列表索引的递推公式：
    node.val node的列表索引 node.left的列表索引	node.right的列表索引

     != null	n	        2(n−m)+1	    2(n−m)+2
     == null	n	        无	            无

    序列化 使用层序遍历实现。反序列化 通过以上递推公式反推各节点在序列中的索引，进而实现。

    序列化 Serialize ：
    借助队列，对二叉树做层序遍历，并将越过叶节点的 null 也打印出来。

    算法流程：
    特例处理： 若 root 为空，则直接返回空列表 "[]" ；
    初始化： 队列 queue （包含根节点 root ）；序列化列表 res ；
    层序遍历： 当 queue 为空时跳出；
    节点出队，记为 node ；
    若 node 不为空：① 打印字符串 node.val ，② 将左、右子节点加入 queue ；
    否则（若 node 为空）：打印字符串 "null" ；
    返回值： 拼接列表，用 ',' 隔开，首尾添加中括号；
    复杂度分析：
    时间复杂度 O(N)O(N) ： NN 为二叉树的节点数，层序遍历需要访问所有节点，最差情况下需要访问 N + 1N+1 个 null ，总体复杂度为 O(2N + 1) = O(N)O(2N+1)=O(N) 。
    空间复杂度 O(N)O(N) ： 最差情况下，队列 queue 同时存储 \frac{N + 1}{2}
    2
    N+1
    ​
      个节点（或 N+1N+1 个 null ），使用 O(N)O(N) ；列表 res 使用 O(N)O(N) 。

    13 / 13

    反序列化 Deserialize ：
    基于本文开始推出的 node , node.left , node.right 在序列化列表中的位置关系，可实现反序列化。

    利用队列按层构建二叉树，借助一个指针 i 指向节点 node 的左、右子节点，每构建一个 node 的左、右子节点，指针 i 就向右移动 11 位。

    算法流程：
    特例处理： 若 data 为空，直接返回 null ；
    初始化： 序列化列表 vals （先去掉首尾中括号，再用逗号隔开），指针 i = 1 ，根节点 root （值为 vals[0] ），队列 queue（包含 root ）；
    按层构建： 当 queue 为空时跳出；
    节点出队，记为 node ；
    构建 node 的左子节点：node.left 的值为 vals[i] ，并将 node.left 入队；
    执行 i += 1 ；
    构建 node 的右子节点：node.left 的值为 vals[i] ，并将 node.left 入队；
    执行 i += 1 ；
    返回值： 返回根节点 root 即可；
    复杂度分析：
    时间复杂度 O(N)O(N) ： NN 为二叉树的节点数，按层构建二叉树需要遍历整个 valsvals ，其长度最大为 2N+12N+1 。
    空间复杂度 O(N)O(N) ： 最差情况下，队列 queue 同时存储 \frac{N + 1}{2}
    2
    N+1
    ​
      个节点，因此使用 O(N)O(N) 额外空间。

    """

    def serialize(self, root):
        if not root: return "[]"
        queue = collections.deque()
        queue.append(root)
        res = []
        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append("null")
        return '[' + ','.join(res) + ']'

    def deserialize(self, data):
        if data == "[]": return
        vals, i = data[1:-1].split(','), 1
        root = TreeNode(int(vals[0]))
        queue = collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if vals[i] != "null":
                node.left = TreeNode(int(vals[i]))
                queue.append(node.left)
            i += 1
            if vals[i] != "null":
                node.right = TreeNode(int(vals[i]))
                queue.append(node.right)
            i += 1
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
if __name__ == '__main__':
    codec = Codec()
    print(codec.deserialize([5, 2, 3, '#', '#', 2, 4, 3, 1, '#', '#', '#', '#', '#', '#']))
    print(codec.deserialize([]))
