"""
实现一个函数，检查一棵二叉树是否为二叉搜索树。

示例1:
输入:
    2
   / \
  1   3
输出: true
示例2:
输入:
    5
   / \
  1   4
    / \
   3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
    根节点的值为 5 ，但是其右子节点值为 4 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/legal-binary-search-tree-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from TreeHelper import TreeNode


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def binary_tree_to_arr(node: TreeNode):
            if not node:
                return []
            return binary_tree_to_arr(node.left) + [node.val] + binary_tree_to_arr(node.right)

        arr = binary_tree_to_arr(root)
        for idx, num in enumerate(arr):
            if idx == 0:
                continue
            if arr[idx] <= arr[idx - 1]:
                return False
        return True
