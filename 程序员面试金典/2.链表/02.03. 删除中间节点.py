"""
若链表中的某个节点，既不是链表头节点，也不是链表尾节点，则称其为该链表的 「中间节点」。
假定已知链表的某一个中间节点，请实现一种算法，将该节点从链表中删除。
例如，传入节点c（位于单向链表a->b->c->d->e->f中），将其删除后，剩余链表为a->b->d->e->f

示例：
输入：节点5（位于单向链表4->5->1->9中）
结果：不返回任何数据，从链表中删除传入的节点 5，使链表变为4->1->9

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/delete-middle-node-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        原始链表:a->b-c-d
        期待结果：删除b，得到a->c->d

        首先把b的值变成c，node.val=node.next.val,那么就会有两个c了，如下
        a->c->c->d

        然后让他跳过第二个c，node.next=node.next.next

        得到a->c->d

        作者：mr-fang-8
        链接：https://leetcode-cn.com/problems/delete-middle-node-lcci/solution/shan-chu-zhong-jian-mou-yi-jie-dian-by-mr-fang-8/
        来源：力扣（LeetCode）
        著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        """
        node.val = node.next.val
        node.next = node.next.next
