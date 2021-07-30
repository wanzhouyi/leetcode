"""
给你二叉树的根结点 root ，请你设计算法计算二叉树的 垂序遍历 序列。
对位于(row, col)的每个结点而言，其左右子结点分别位于(row + 1, col - 1)和(row + 1, col + 1) 。
树的根结点位于 (0, 0) 。
二叉树的 垂序遍历 从最左边的列开始直到最右边的列结束，按列索引每一列上的所有结点，形成一个按出现位置从上到下排序的有序列表。
如果同行同列上有多个结点，则按结点的值从小到大进行排序。
返回二叉树的 垂序遍历 序列。

示例 1：

输入：root = [3,9,20,null,null,15,7]
输出：[[9],[3,15],[20],[7]]
解释：
列 -1 ：只有结点 9 在此列中。
列  0 ：只有结点 3 和 15 在此列中，按从上到下顺序。
列  1 ：只有结点 20 在此列中。
列  2 ：只有结点 7 在此列中。
示例 2：

输入：root = [1,2,3,4,5,6,7]
输出：[[4],[2],[1,5,6],[3],[7]]
解释：
列 -2 ：只有结点 4 在此列中。
列 -1 ：只有结点 2 在此列中。
列  0 ：结点 1 、5 和 6 都在此列中。
          1 在上面，所以它出现在前面。
          5 和 6 位置都是 (2, 0) ，所以按值从小到大排序，5 在 6 的前面。
列  1 ：只有结点 3 在此列中。
列  2 ：只有结点 7 在此列中。
示例 3：


输入：root = [1,2,3,4,6,5,7]
输出：[[4],[2],[1,5,6],[3],[7]]
解释：
这个示例实际上与示例 2 完全相同，只是结点 5 和 6 在树中的位置发生了交换。
因为 5 和 6 的位置仍然相同，所以答案保持不变，仍然按值从小到大排序。


提示：

树中结点数目总数在范围 [1, 1000] 内
0 <= Node.val <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/vertical-order-traversal-of-a-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for a binary tree node.
from collections import defaultdict
from typing import List
from sortedcontainers import SortedDict, SortedList
from BinaryTreeHelper import TreeNode, create_tree


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        dic = SortedDict()

        def dfs(node: TreeNode, x, y):
            if not node:
                return
            if y in dic.keys():
                dic[y].append((x, node.val))
            else:
                dic.setdefault(y, [(x, node.val)])

            if node.left:
                dfs(node.left, x + 1, y - 1)
            if node.right:
                dfs(node.right, x + 1, y + 1)

        dfs(root, 0, 0)
        print(dic)
        ans = []
        for key in dic:
            ls = dic[key]
            ls.sort(key=lambda x: (x[0], x[1]))
            ans.append(list(map(lambda x: x[1], ls)))
        return ans


# 官解
class Solution:
    """
    方法一：自定义排序
    思路与算法

    我们可以从根节点开始，对整棵树进行一次遍历，在遍历的过程中使用数组 \textit{nodes}nodes 记录下每个节点的行号 \textit{row}row，列号 \textit{col}col 以及值 \textit{value}value。在遍历完成后，我们按照 \textit{col}col 为第一关键字升序，\textit{row}row 为第二关键字升序，\textit{value}value 为第三关键字升序，对所有的节点进行排序即可。

    在排序完成后，我们还需要按照题目要求，将同一列的所有节点放入同一个数组中。因此，我们可以对 \textit{nodes}nodes 进行一次遍历，并在遍历的过程中记录上一个节点的列号 \textit{lastcol}lastcol。如果当前遍历到的节点的列号 \textit{col}col 与 \textit{lastcol}lastcol 相等，则将该节点放入与上一个节点相同的数组中，否则放入不同的数组中。

    作者：LeetCode-Solution
    链接：https://leetcode-cn.com/problems/vertical-order-traversal-of-a-binary-tree/solution/er-cha-shu-de-chui-xu-bian-li-by-leetcod-clsh/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        nodes = list()

        def dfs(node: TreeNode, row: int, col: int) -> None:
            if not node:
                return

            nodes.append((col, row, node.val))
            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)

        dfs(root, 0, 0)
        nodes.sort()
        ans, lastcol = list(), float("-inf")

        for col, row, value in nodes:
            if col != lastcol:
                lastcol = col
                ans.append(list())
            ans[-1].append(value)

        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.verticalTraversal(create_tree('[3,9,20,null,null,null,15,7]')))
