"""
从左向右遍历一个数组，通过不断将其中的元素插入树中可以逐步地生成一棵二叉搜索树。给定一个由不同节点组成的二叉搜索树，输出所有可能生成此树的数组。



示例：
给定如下二叉树

        2
       / \
      1   3
返回：

[
   [2,1,3],
   [2,3,1]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/bst-sequences-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List

from TreeHelper import TreeNode


class Solution:
    """
    使用一个queue存储下个所有可能的节点
    然后选择其中一个作为path的下一个元素
    递归直到queue元素为空
    将对应的path加入结果中
    由于二叉搜索树没有重复元素, 而且每次递归的使用元素的顺序都不一样, 所以自动做到了去重

    作者：suibianfahui
    链接：https://leetcode-cn.com/problems/bst-sequences-lcci/solution/15xing-dai-ma-by-suibianfahui/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def BSTSequences(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return [[]]
        res = []

        def findPath(cur, q, path):
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
            if not q:
                res.append(path)
                return
            for i, nex in enumerate(q):
                newq = q[:i] + q[i + 1:]
                findPath(nex, newq, path + [nex.val])

        findPath(root, [], [root.val])
        return res
