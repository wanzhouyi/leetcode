"""
给定一棵二叉树，其中每个节点都含有一个整数数值(该值或正或负)。设计一个算法，打印节点数值总和等于某个给定值的所有路径的数量。注意，路径不一定非得从二叉树的根节点或叶节点开始或结束，但是其方向必须向下(只能从父节点指向子节点方向)。

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:

3
解释：和为 22 的路径有：[5,4,11,2], [5,8,4,5], [4,11,7]
提示：

节点总数 <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/paths-with-sum-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from TreeHelper import TreeNode, create_tree


class Solution:
    """利用树路径的前缀和"""

    def pathSum(self, root: TreeNode, sum: int) -> int:
        path = [0]
        ans = 0

        def dfs(node: TreeNode, node_path: list):
            if not node:
                return
            pre_sum = node_path[-1] + node.val
            ct = node_path.count(pre_sum - sum)
            nonlocal ans
            ans += ct
            node_path.append(pre_sum)
            dfs(node.left, node_path.copy())
            dfs(node.right, node_path.copy())

        dfs(root, path)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.pathSum(create_tree('[5,4,8,11,null,13,4,7,2,null,null,5,1]'), 22))
