"""
实现一个函数，检查二叉树是否平衡。在这个问题中，平衡树的定义如下：任意一个节点，其两棵子树的高度差不超过 1。


示例 1:
给定二叉树 [3,9,20,null,null,15,7]
    3
   / \
  9  20
    /  \
   15   7
返回 true 。
示例 2:
给定二叉树 [1,2,2,3,3,null,null,4,4]
      1
     / \
    2   2
   / \
  3   3
 / \
4   4
返回 false 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/check-balance-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from TreeHelper import TreeNode, create_tree


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def judge(node: TreeNode, depth_judge):
            if not node.left and not node.right:
                return depth_judge, True
            elif node.left and node.right:
                ldepth, l_result = judge(node.left, depth_judge + 1)
                rdepth, r_result = judge(node.right, depth_judge + 1)
                if abs(ldepth - rdepth) <= 1 and l_result and r_result:
                    return max(ldepth, rdepth), True
                else:
                    return max(ldepth, rdepth), False
            else:
                if node.left and not node.right:
                    ldepth, l_result = judge(node.left, depth_judge + 1)
                    if ldepth - depth_judge <= 1 and l_result:
                        return ldepth, True
                    else:
                        return ldepth, False
                elif node.right and not node.left:
                    rdepth, r_result = judge(node.right, depth_judge + 1)
                    if rdepth - depth_judge <= 1 and r_result:
                        return rdepth, True
                    else:
                        return rdepth, False

        if not root:
            return True
        depth, result = judge(root, 0)
        return result


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        """自顶向下"""

        def height(root: TreeNode) -> int:
            if not root:
                return 0
            return max(height(root.left), height(root.right)) + 1

        if not root:
            return True
        return abs(height(root.left) - height(root.right)) <= 1 and self.isBalanced(
            root.left) and self.isBalanced(root.right)


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        """自底向上"""

        def height(root: TreeNode) -> int:
            if not root:
                return 0
            leftHeight = height(root.left)
            rightHeight = height(root.right)
            if leftHeight == -1 or rightHeight == -1 or abs(leftHeight - rightHeight) > 1:
                return -1
            else:
                return max(leftHeight, rightHeight) + 1

        return height(root) >= 0


if __name__ == '__main__':
    s = Solution()
    print(s.isBalanced(create_tree('[3,9,20,null,null,15,7]')))
    # print(s.isBalanced(create_tree('[]')))
    print(s.isBalanced(create_tree('[1,2]')))
