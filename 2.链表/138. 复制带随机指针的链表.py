"""
给你一个长度为 n 的链表，每个节点包含一个额外增加的随机指针 random ，该指针可以指向链表中的任何节点或空节点。
构造这个链表的深拷贝。深拷贝应该正好由 n 个 全新 节点组成，其中每个新节点的值都设为其对应的原节点的值。新节点的 next 指针和 random 指针也都应指向复制链表中的新节点，并使原链表和复制链表中的这些指针能够表示相同的链表状态。复制链表中的指针都不应指向原链表中的节点 。
例如，如果原链表中有 X 和 Y 两个节点，其中 X.random --> Y 。那么在复制链表中对应的两个节点 x 和 y ，同样有 x.random --> y 。
返回复制链表的头节点。
用一个由n个节点组成的链表来表示输入/输出中的链表。每个节点用一个[val, random_index]表示：
val：一个表示Node.val的整数。
random_index：随机指针指向的节点索引（范围从0到n-1）；如果不指向任何节点，则为null。
你的代码 只 接受原链表的头节点 head 作为传入参数。
示例 1：
输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]
示例 2：
输入：head = [[1,1],[2,1]]
输出：[[1,1],[2,1]]
示例 3：
输入：head = [[3,null],[3,0],[3,null]]
输出：[[3,null],[3,0],[3,null]]
示例 4：
输入：head = []
输出：[]
解释：给定的链表为空（空指针），因此返回 null。

提示：
0 <= n <= 1000
-10000 <= Node.val <= 10000
Node.random为空（null）或指向链表中的节点。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/copy-list-with-random-pointer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        shadow_head = head
        src_nodes = []
        nodes = []
        index = 0
        while shadow_head:
            if not nodes:
                nodes.append(Node(shadow_head.val))
            else:
                new_node = Node(shadow_head.val)
                nodes[-1].next = new_node
                nodes.append(new_node)
            src_nodes.append(shadow_head)

            shadow_head = shadow_head.next

        shadow_head_1 = head
        index_1 = 0
        while shadow_head_1:
            ran = shadow_head_1.random
            if ran:
                idx = src_nodes.index(ran)
                nodes[index_1].random = nodes[idx]
            shadow_head_1 = shadow_head_1.next
            index_1 += 1
        return nodes[0]


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return
        dic = {}
        cur = head
        while cur:
            dic[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:
            dic[cur].next = dic.get(cur.next)
            dic[cur].random = dic.get(cur.random)
            cur = cur.next
        return dic[head]


if __name__ == '__main__':
    s = Solution()
    root = Node(0)
    head = root
    inputs = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
    nodes = []
    for node in inputs:
        nodes.append(Node(node[0]))
    for idx, node in enumerate(inputs):
        if idx < len(inputs) - 1:
            nodes[idx].next = nodes[idx + 1]
        if node[1] is not None:
            nodes[idx].random = nodes[node[1]]
    print(s.copyRandomList(nodes[0]))
