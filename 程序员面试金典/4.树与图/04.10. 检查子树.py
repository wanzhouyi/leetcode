"""
检查子树。你有两棵非常大的二叉树：T1，有几万个节点；T2，有几万个节点。设计一个算法，判断 T2 是否为 T1 的子树。

如果 T1 有这么一个节点 n，其子树与 T2 一模一样，则 T2 为 T1 的子树，也就是说，从节点 n 处把树砍断，得到的树与 T2 完全相同。

注意：此题相对书上原题略有改动。

示例1:

 输入：t1 = [1, 2, 3], t2 = [2]
 输出：true
示例2:

 输入：t1 = [1, null, 2, 4], t2 = [3, 2]
 输出：false
提示：

树的节点数目范围为[0, 20000]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/check-subtree-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from TreeHelper import TreeNode


class Solution:
    """
    利用前序遍历后对数组进行切片
    """

    def checkSubTree(self, t1: TreeNode, t2: TreeNode) -> bool:
        def pre_order(node):
            if not node:
                return []

            return [node.val] + pre_order(node.left) + pre_order(node.right)

        t1_arr = pre_order(t1)
        t2_arr = pre_order(t2)
        print(t1_arr, t2_arr)

        nt1, nt2 = len(t1_arr), len(t2_arr)
        for i in range(nt1 - nt2 + 1):
            if t1_arr[i:i + nt2] == t2_arr:
                return True
        return False


class Solution:
    """
    第一重：在 t1 中找到 t2 的起点。先判断 t1 当前节点，如果不对就判断 t1 左子树和 t1 右子树。
    第二重：从找到的起点开始判断剩下的点，t1 和 t2 同步左右子树搜索。

    作者：wonz
    链接：https://leetcode-cn.com/problems/check-subtree-lcci/solution/liang-zhong-dfspython3-by-wonz5130-2/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def checkSubTree(self, t1: TreeNode, t2: TreeNode) -> bool:
        if t1 == None:
            return not t2
        if t2 == None:
            return True
        # find the root of t2 in t1
        return self.dfs(t1, t2) or self.checkSubTree(t1.left, t2) or self.checkSubTree(t1.right, t2)

    def dfs(self, t1, t2):
        # t2 is over
        if t2 == None:
            return True
        # t2 is not over and t1 is over
        elif t2 != None and t1 == None:
            return False
        # not equal
        elif t2.val != t1.val:
            return False
        # equal, then search left and right
        else:
            return self.dfs(t1.left, t2.left) and self.dfs(t1.right, t2.right)  # 注意这里是and


class Solution:
    """
    解题思路
    什么对称树，相同树，完全子树，一半子树，答案都是一样的
    如果都为空的时候，也是可以认为是对方的子树，所以返回True
    """

    def checkSubTree(self, t1: TreeNode, t2: TreeNode) -> bool:
        def dfs(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            return t1.val == t2.val and dfs(t1.left, t2.left) and dfs(t1.right, t2.right)

        # 都为空？
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        if dfs(t1, t2):
            return True
        return self.checkSubTree(t1.left, t2) or self.checkSubTree(t1.right, t2)
