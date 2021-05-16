"""
给定一棵二叉树，设计一个算法，创建含有某一深度上所有节点的链表（比如，若一棵树的深度为 D，则会创建出 D 个链表）。返回一个包含所有深度的链表的数组。

 

示例：

输入：[1,2,3,4,5,null,7,8]

        1
       /  \
      2    3
     / \    \
    4   5    7
   /
  8

输出：[[1],[2,3],[4,5,7],[8]]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/list-of-depth-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


from typing import List

from TreeHelper import TreeNode


class Solution:
    def listOfDepth(self, tree: TreeNode) -> List[ListNode]:
        ans = []
        stack = [tree]
        while stack:
            tmp_stack = stack.copy()
            stack.clear()
            root = head = TreeNode(None)
            for node in tmp_stack:
                head.next = ListNode(node.val)
                head = head.next
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            ans.append(root.next)
        return ans
