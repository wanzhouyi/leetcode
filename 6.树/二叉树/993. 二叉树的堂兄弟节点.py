"""
在二叉树中，根节点位于深度 0 处，每个深度为 k 的节点的子节点位于深度 k+1 处。

如果二叉树的两个节点深度相同，但 父节点不同 ，则它们是一对堂兄弟节点。

我们给出了具有唯一值的二叉树的根节点 root ，以及树中两个不同节点的值 x 和 y 。

只有与值 x 和 y 对应的节点是堂兄弟节点时，才返回 true 。否则，返回 false。



示例 1：


输入：root = [1,2,3,4], x = 4, y = 3
输出：false
示例 2：


输入：root = [1,2,3,null,4,null,5], x = 5, y = 4
输出：true
示例 3：



输入：root = [1,2,3,null,4], x = 2, y = 3
输出：false


提示：

二叉树的节点数介于2 到100之间。
每个节点的值都是唯一的、范围为1 到100的整数。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/cousins-in-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from BinaryTreeHelper import TreeNode


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        stack = [root]
        while stack:
            tmp_stack = stack.copy()
            stack.clear()
            level = set()
            for node in tmp_stack:
                if node.left:
                    stack.append(node.left)
                    lft = node.left.val
                    level.add(lft)
                if node.right:
                    stack.append(node.right)
                    rht = node.right.val
                    level.add(rht)

                if node.left and node.right and x in (lft, rht) and y in (lft, rht):
                    return False

            if x in level and y in level:
                return True
            elif x in level and y not in level:
                return False
            elif y in level and x not in level:
                return False
        return False
