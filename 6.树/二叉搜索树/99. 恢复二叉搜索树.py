"""
给你二叉搜索树的根节点 root ，该树中的两个节点被错误地交换。请在不改变其结构的情况下，恢复这棵树。
进阶：使用 O(n) 空间复杂度的解法很容易实现。你能想出一个只使用常数空间的解决方案吗？

示例 1：
输入：root = [1,3,null,null,2]
输出：[3,1,null,null,2]
解释：3 不能是 1 左孩子，因为 3 > 1 。交换 1 和 3 使二叉搜索树有效。

示例 2：
输入：root = [3,1,4,null,null,2]
输出：[2,1,4,null,null,3]
解释：2 不能在 3 的右子树中，因为 2 < 3 。交换 2 和 3 使二叉搜索树有效。

提示：

树上节点的数目在范围 [2, 1000] 内
-2^31 <= Node.val <= 2^31 - 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/recover-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def mid_sort(node: TreeNode):
            if not node:
                return []
            return mid_sort(node.left) + [node.val] + mid_sort(node.right)

        mid_order = mid_sort(root)
        # print(mid_order)
        sorted_mid_order = sorted(mid_order)
        # print(sorted_mid_order)
        rep = []
        for i in range(len(sorted_mid_order)):
            if mid_order[i] != sorted_mid_order[i]:
                rep = [mid_order[i], sorted_mid_order[i]]
                break

        def replace(node):
            if not node:
                return

            if node.val == rep[0]:
                node.val = rep[1]
            elif node.val == rep[1]:
                node.val = rep[0]

            replace(node.left)
            replace(node.right)

        replace(root)


# 解法
class Solution(object):
    """
    解法一
    注意题目给出的条件，是 二叉搜索树，这就是意味着节点之间是有顺序关系的。
    如果我们把整棵树都 遍历 一遍，将遍历的结果保存下来，比如放到一个数组中。
    那么这个数组应该是有序的。

    既然是有序的那就好办了，我们将这个有序的数组遍历一遍。
    如果数组是完全有序的，那么直接返回就可以了。
    否则，我们找到顺序不一致的两个下标i和j，将arr[i].val和arr[j].val的值互换一下即可。

    作者：wang_ni_ma
    链接：https://leetcode-cn.com/problems/recover-binary-search-tree/solution/san-chong-jie-fa-xiang-xi-tu-jie-99-hui-fu-er-cha-/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def recoverTree(self, root):
        nodes = []

        # 中序遍历二叉树，并将遍历的结果保存到list中
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            nodes.append(root)
            dfs(root.right)

        dfs(root)
        x = None
        y = None
        pre = nodes[0]
        # 扫面遍历的结果，找出可能存在错误交换的节点x和y
        for i in range(1, len(nodes)):
            if pre.val > nodes[i].val:
                y = nodes[i]
                if not x:
                    x = pre
            pre = nodes[i]
        # 如果x和y不为空，则交换这两个节点值，恢复二叉搜索树
        if x and y:
            x.val, y.val = y.val, x.val
