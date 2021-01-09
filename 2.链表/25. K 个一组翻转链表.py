"""
给你一个链表，每k个节点一组进行翻转，请你返回翻转后的链表。
k是一个正整数，它的值小于或等于链表的长度。
如果节点总数不是k的整数倍，那么请将最后剩余的节点保持原有顺序。

示例：
给你这个链表：1->2->3->4->5
当k= 2 时，应当返回: 2->1->4->3->5
当k= 3 时，应当返回: 3->2->1->4->5

说明：
你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-nodes-in-k-group
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 方法一，模拟，64ms，29%
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def reverse_sub(head):
            new_head = ListNode(None)
            new_head.next = head
            current = new_head.next

            while current and current.next:
                nxt = current.next
                current.next = nxt.next
                nxt.next = new_head.next
                new_head.next = nxt

            current.next = None
            return new_head.next, current

        dummy = ListNode(None)
        dummy.next = head
        pre = dummy
        current = dummy.next

        counter = 0
        while current:
            counter += 1

            if counter == k:
                counter = 0
                nxt = current.next
                current.next = None
                group_head, group_last = reverse_sub(pre.next)
                pre.next = group_head

                group_last.next = nxt
                pre = group_last
                current = group_last

            current = current.next
        return dummy.next
