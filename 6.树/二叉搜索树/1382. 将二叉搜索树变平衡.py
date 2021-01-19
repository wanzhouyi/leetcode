"""
给你一棵二叉搜索树，请你返回一棵平衡后的二叉搜索树，新生成的树应该与原来的树有着相同的节点值。
如果一棵二叉搜索树中，每个节点的两棵子树高度差不超过 1 ，我们就称这棵二叉搜索树是平衡的 。
如果有多种构造方法，请你返回任意一种。

示例：

输入：root = [1,null,2,null,3,null,4,null,null]
输出：[2,1,3,null,null,null,4]
解释：这不是唯一的正确答案，[3,1,4,null,2,null,null] 也是一个可行的构造方案。

提示：

树节点的数目在1到10^4之间。
树节点的值互不相同，且在1到10^5 之间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/balance-a-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List

from BinaryTreeHelper import TreeNode


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def inorder(root):
            if not root:
                return []
            return inorder(root.left) + [root] + inorder(root.right)

        stack = inorder(root)

        def create_BST(stack: List):
            if not stack:
                return None
            mid = len(stack) // 2
            mid_node = stack[mid]
            mid_node.left = create_BST(stack[:mid])
            mid_node.right = create_BST(stack[mid + 1:])
            return mid_node

        return create_BST(stack)
