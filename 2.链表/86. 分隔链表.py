"""
给你一个链表和一个特定值 x ，请你对链表进行分隔，使得所有小于 x 的节点都出现在大于或等于 x 的节点之前。
你应当保留两个分区中每个节点的初始相对位置。

示例：

输入：head = 1->4->3->2->5->2, x = 3
输出：1->2->2->4->3->5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/partition-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from ListNodeHelper import ListNode, create_listnode, listnode_to_list


class Solution:
    # 方法一，打散链表
    def partition(self, head: ListNode, x: int) -> ListNode:
        """
        如果题目中没明确说明在原链表上操作，可以打散成单个节点，再组装成链表。这样和人的思维方式一致，简单易处理。
        """
        # 添加哨兵节点，方便处理
        less_dummy = ListNode(None)
        less_current = less_dummy
        great_dummy = ListNode(None)
        great_current = great_dummy
        while head:
            if head.val < x:
                less_current.next = head
                less_current = less_current.next
            else:
                great_current.next = head
                great_current = great_current.next
            head = head.next
        great_current.next = None
        less_current.next = great_dummy.next
        return less_dummy.next

    # 方法二，原地操作节点
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return None
        dummy = ListNode(0)
        dummy.next = head

        before = None
        pre = None
        current = head

        while current:
            if current.val < x and pre and pre.val >= x:
                if not before:
                    before = dummy
                nxt = current.next
                pre.next = nxt
                current.next = before.next
                before.next = current
                before = current
                current = nxt
            else:
                if current.val < x:
                    before = current
                pre = current
                current = current.next
        return dummy.next


if __name__ == '__main__':
    s = Solution()
    # 头节点比X小的情况
    print(listnode_to_list(s.partition(create_listnode([1, 4, 3, 2, 5, 2]), 3)))
    # 头节点比X大的情况
    print(listnode_to_list(s.partition(create_listnode([4, 3, 1, 2, 5, 2]), 3)))
