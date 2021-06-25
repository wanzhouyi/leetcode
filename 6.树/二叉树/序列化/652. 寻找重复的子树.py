"""
给定一棵二叉树，返回所有重复的子树。对于同一类的重复子树，你只需要返回其中任意一棵的根结点即可。

两棵树重复是指它们具有相同的结构以及相同的结点值。

示例 1：

        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4
下面是两个重复的子树：

      2
     /
    4
和

    4
因此，你需要以列表的形式返回上述重复子树的根结点。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-duplicate-subtrees
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for a binary tree node.
import collections
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        dic = dict()
        ans = []

        def serilize(node: TreeNode):
            if not node:
                return '#'
            # 序列化以当前节点为根节点的二叉树
            str_ser = '{},{},{}'.format(serilize(node.left), node.val, serilize(node.right))
            # 使用一个HashMap来记录所有的子树的序列
            if not dic.get(str_ser):
                dic[str_ser] = 1
            elif dic[str_ser] == 1:
                dic[str_ser] += 1
                ans.append(node)
            else:
                pass

        serilize(root)
        return ans


class Solution(object):
    """
    方法一：深度优先搜索【通过】
    思路

    序列化二叉树。

    Python

       1
      / \
     2   3
        / \
       4   5
    例如上面这棵树序列化结果为 1,2,#,#,3,4,#,#,5,#,#。每棵不同子树的序列化结果都是唯一的。

    算法

    使用深度优先搜索，其中递归函数返回当前子树的序列化结果。把每个节点开始的子树序列化结果保存在 mapmap 中，然后判断是否存在重复的子树。

    作者：LeetCode
    链接：https://leetcode-cn.com/problems/find-duplicate-subtrees/solution/xun-zhao-zhong-fu-de-zi-shu-by-leetcode/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def findDuplicateSubtrees(self, root):
        count = collections.Counter()
        ans = []

        def collect(node):
            if not node: return "#"
            serial = "{},{},{}".format(node.val, collect(node.left), collect(node.right))
            count[serial] += 1
            if count[serial] == 2:
                ans.append(node)
            return serial

        collect(root)
        return ans


class Solution(object):
    """
    方法二：唯一标识符【通过】
    思路

    假设每棵子树都有一个唯一标识符：只有当两个子树的 id 相同时，认为这两个子树是相同的。

    一个节点 node 的左孩子 id 为 x，右孩子 id 为 y，那么该节点的 id 为 (node.val, x, y)。

    算法

    如果三元组 (node.val, x, y) 第一次出现，则创建一个这样的三元组记录该子树。如果已经出现过，则直接使用该子树对应的 id。

    作者：LeetCode
    链接：https://leetcode-cn.com/problems/find-duplicate-subtrees/solution/xun-zhao-zhong-fu-de-zi-shu-by-leetcode/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def findDuplicateSubtrees(self, root):
        trees = collections.defaultdict()
        trees.default_factory = trees.__len__
        count = collections.Counter()
        ans = []

        def lookup(node):
            if node:
                uid = trees[node.val, lookup(node.left), lookup(node.right)]
                count[uid] += 1
                if count[uid] == 2:
                    ans.append(node)
                return uid

        lookup(root)
        return ans
