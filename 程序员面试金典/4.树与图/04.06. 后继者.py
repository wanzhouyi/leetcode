"""
设计一个算法，找出二叉搜索树中指定节点的“下一个”节点（也即中序后继）。
如果指定节点没有对应的“下一个”节点，则返回null。
示例 1:
输入: root = [2,1,3], p = 1

  2
 / \
1   3

输出: 2
示例 2:
输入: root = [5,3,6,2,4,null,null,1], p = 6

      5
     / \
    3   6
   / \
  2   4
 /
1

输出: null

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/successor-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from TreeHelper import TreeNode


class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        """暴力解法，利用了中序遍历"""

        def binary_tree_to_arr(node: TreeNode):
            if not node:
                return []
            return binary_tree_to_arr(node.left) + [node.val] + binary_tree_to_arr(node.right)

        arr = binary_tree_to_arr(root)
        p_idx = arr.index(p.val)
        if p_idx >= len(arr) - 1:
            return None
        else:
            next_val = arr[p_idx + 1]
            current = root
            while current:
                if current.val == next_val:
                    return current
                elif current.val >= next_val:
                    current = current.left
                else:
                    current = current.right


class Solution:
    """
    所谓 p 的后继节点，就是这串升序数字中，比 p 大的下一个。

    如果 p 大于当前节点的值，说明后继节点一定在 RightTree
    如果 p 等于当前节点的值，说明后继节点一定在 RightTree
    如果 p 小于当前节点的值，说明后继节点一定在 LeftTree 或自己就是
    递归调用 LeftTree，如果是空的，说明当前节点就是答案
    如果不是空的，则说明在 LeftTree 已经找到合适的答案，直接返回即可

    """

    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        if root:
            if p.val >= root.val:
                return self.inorderSuccessor(root.right, p)
            else:
                if self.inorderSuccessor(root.left, p) is None:
                    return root
                else:
                    return self.inorderSuccessor(root.left, p)
        return None
