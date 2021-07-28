"""
给定一个二叉树（具有根结点root），一个目标结点target，和一个整数值 K 。
返回到目标结点 target 距离为 K 的所有结点的值的列表。 答案可以以任何顺序返回。
示例 1：
输入：root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2
输出：[7,4,1]
解释：
所求结点为与目标结点（值为 5）距离为 2 的结点，
值分别为 7，4，以及 1
注意，输入的 "root" 和 "target" 实际上是树上的结点。
上面的输入仅仅是对这些对象进行了序列化描述。
提示：

给定的树是非空的。
树上的每个结点都具有唯一的值0 <= node.val <= 500。
目标结点target是树上的结点。
0 <= K <= 1000.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/all-nodes-distance-k-in-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for a binary tree node.
import collections
from collections import defaultdict, deque
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        ps = None

        def get_path(node: TreeNode, path: list):
            nonlocal ps
            if ps:
                return
            if not node:
                return
            if node == target:
                ps = path.copy()
                return
            if node.left:
                path.append(node.left)
                get_path(node.left, path)
                path.pop()
            if node.right:
                path.append(node.right)
                get_path(node.right, path)
                path.pop()

        get_path(root, [root])

        # print([node.val for node in ps])

        def get_children(node: TreeNode, level: int):
            if level < 0:
                return []
            # print('111',node.val,level)
            stack_node = [node]
            while stack_node and level > 0:
                stack_node_cp = stack_node.copy()
                stack_node.clear()
                for node in stack_node_cp:
                    if node.left and node.left not in ps:
                        stack_node.append(node.left)
                    if node.right and node.right not in ps:
                        stack_node.append(node.right)
                level -= 1
                # print('222',[node.val for node in stack_node])

            return [node.val for node in stack_node]

        ans = []
        n = len(ps)
        for idx, node in enumerate(ps):
            ans.extend(get_children(node, k - (n - idx - 1)))

        # print(ans)
        return ans


# 优秀的解法
class Solution:
    """
    先构造一个连通图，每一个节点，作为key，value是节点的相邻节点列表
    图建好之后，用 BFS 去遍历
    过程中需要一个 visited 集合去存已经遍历过的节点，避免重复算

    作者：niconiconi-12
    链接：https://leetcode-cn.com/problems/all-nodes-distance-k-in-binary-tree/solution/chi-xiao-dou-python-bfs-hashmap-dai-ma-j-d3kl/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        graph = defaultdict(list)

        # 巧妙之处，有parent才去构建连通关系
        # 注意这里需要传一个parent node，否则数字无法判断是否None
        def build_graph(root, parent):
            if root is None:
                return
            nonlocal graph
            if parent:
                graph[parent.val].append(root.val)
                graph[root.val].append(parent.val)
            build_graph(root.left, root)
            build_graph(root.right, root)

        build_graph(root, None)

        ans = []
        visited = set([target.val])
        queue = deque([target.val])

        # BFS 的经典遍历方法
        while queue:
            queue_len = len(queue)
            # 当 k 为0 则输出
            if k == 0:
                for i in range(queue_len):
                    curr = queue.popleft()
                    ans.append(curr)
                return ans

            for i in range(queue_len):
                curr = queue.popleft()
                for n in graph[curr]:
                    if n not in visited:
                        queue.append(n)
                        visited.add(n)

            k -= 1

        return ans


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # ----------------- 当成图，构建邻接表中尚未构建的部分。---------------------#
        node_parent = dict()

        def dfs_find_parent(node: TreeNode) -> None:
            if node:
                if node.left:
                    node_parent[node.left] = node
                if node.right:
                    node_parent[node.right] = node
                dfs_find_parent(node.left)
                dfs_find_parent(node.right)

        dfs_find_parent(root)

        # ---------------- bfs波纹法， 先visit&先判适应于距离大于1

        # ---- k == 0
        if k == 0:
            return [target.val]

        res = []

        Q = collections.deque()
        visited = set()
        Q.append(target)
        visited.add(target)  # 先visit
        level = 0
        while Q and level < k:
            level += 1
            for _ in range(len(Q)):
                x = Q.popleft()
                for y in [node_parent[x] if x in node_parent else None, x.left, x.right]:
                    if y and y not in visited:
                        if level == k:
                            res.append(y.val)  # 先判
                        Q.append(y)
                        visited.add(y)

        return res
