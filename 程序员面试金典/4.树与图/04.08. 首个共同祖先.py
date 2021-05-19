"""
设计并实现一个算法，找出二叉树中某两个节点的第一个共同祖先。不得将其他的节点存储在另外的数据结构中。
注意：这不一定是二叉搜索树。

例如，给定如下二叉树: root = [3,5,1,6,2,0,8,null,null,7,4]

    3
   / \
  5   1
 / \ / \
6  2 0  8
  / \
 7   4
示例 1:

输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出: 3
解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
示例 2:

输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出: 5
解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。
说明:

所有节点的值都是唯一的。
p、q 为不同节点且均存在于给定的二叉树中。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/first-common-ancestor-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from TreeHelper import TreeNode, create_tree


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """深度优先遍历，能过，性能差"""
        p_path, q_path = None, None

        def dfs(node: TreeNode, path: list):
            if not node:
                return
            nonlocal p_path, q_path
            if p_path and q_path:
                return
            path.append(node)
            if node.val == p.val:
                p_path = path.copy()
            elif node.val == q.val:
                q_path = path.copy()
            dfs(node.left, path.copy())
            dfs(node.right, path.copy())

        dfs(root, [])
        while p_path:
            top = p_path.pop()
            if top in q_path:
                return top
        return None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        假设我们从跟结点开始，采用 DFS 向下遍历，如果当前结点到达叶子结点下的空结点时，返回空；如果当前结点为 p 或 q 时，返回当前结点；

        这样，当我们令 left = self.lowestCommonAncestor(root.left, p, q) 时，如果在左子树中找到了 p 或 q，left 会等于 p 或 q，同理，right 也是一样；

        然后我们进行判断：如果 left 为 right 都不为空，则为情况 1；如果 left 和 right 中只有一个不为空，说明这两个结点在子树中，则根节点到达子树再进行寻找。

        作者：z1m
        链接：https://leetcode-cn.com/problems/first-common-ancestor-lcci/solution/di-gui-jie-fa-python-3-c-by-z1m/
        来源：力扣（LeetCode）
        著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        """
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right: return root
        return left if left else right


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        思路
        分析
            对于当前的根节点root
                若root为空，直接返回root，表示没有找到目标
                若root为p或q
                    若左子树或右子树中含有另外一个目标节点，那么root就是最终答案，返回root
                    否则，也应当返回root，表示找到了其中一个目标
                否则
                    若左子树和右子树分别含有p、q中的一个，那么root就是最终答案，返回root
                    否则
                        若两子树中含有p或q中的一个，即返回那个节点，表示找到了其中一个目标
                        否则返回nullptr，表示没有找到目标
        整理
            经过整理我们发现
                若root为p或q，无论子树是否含有另外一个目标，都应该返回root
                另外，当左右子树的均含有目标节点时，返回root，否则只需返回找到的目标节点或空指针
        算法
            若root为空或root == p或root == q，返回root
            分别将root->left、root->right作为根节点，调用自身，得到返回值left、right
            若left不为空
                若right不为空，返回root
                否则返回left
            否则返回right

        作者：mimosys
        链接：https://leetcode-cn.com/problems/first-common-ancestor-lcci/solution/c-java-python-mian-shi-ti-0408-shou-ge-gong-tong-z/
        来源：力扣（LeetCode）
        著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        """
        if not root or root == p or root == q: return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        return (root if right else left) if left else right


if __name__ == '__main__':
    s = Solution()
    # print(s.lowestCommonAncestor(create_tree('[3,5,1,6,2,0,8,null,null,7,4]'),TreeNode(5),TreeNode(1)))
    print(s.lowestCommonAncestor(create_tree('[3,5,1,6,2,0,8,null,null,7,4]'), TreeNode(5),
                                 TreeNode(4)))
