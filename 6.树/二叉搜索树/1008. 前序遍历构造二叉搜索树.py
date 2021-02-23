"""
返回与给定前序遍历preorder 相匹配的二叉搜索树（binary search tree）的根结点。
(回想一下，二叉搜索树是二叉树的一种，其每个节点都满足以下规则，对于node.left的任何后代，值总 < node.val，
而 node.right 的任何后代，值总 > node.val。此外，前序遍历首先显示节点node 的值，
然后遍历 node.left，接着遍历 node.right。）
题目保证，对于给定的测试用例，总能找到满足要求的二叉搜索树。

示例：

输入：[8,5,1,7,10,12]
输出：[8,5,10,1,7,null,12]

提示：

1 <= preorder.length <= 100
1 <= preorder[i]<= 10^8
preorder 中的值互不相同

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/construct-binary-search-tree-from-preorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        midorder = sorted(preorder)

        def createTree(pre, mid):
            if not pre or not mid:
                return None

            root = TreeNode(pre[0])
            index_root = mid.index(pre[0])
            root.left = createTree(pre[1:index_root + 1], mid[:index_root])
            root.right = createTree(pre[index_root + 1:], mid[index_root + 1:])
            return root

        return createTree(preorder, midorder)
