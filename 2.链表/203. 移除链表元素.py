"""
删除链表中等于给定值 val 的所有节点。

示例:
输入: 1->2->6->3->4->5->6, val = 6
输出: 1->2->3->4->5
"""
from ListNodeHelper import ListNode, create_listnode, listnode_to_list


class Solution:
    # 方法一， 遍历， 72ms
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        """
        通常链表操作都会添加一个哨兵节点，能显著降低边界条件判断的复杂度
        """
        dummy = ListNode(None)
        dummy.next = head
        pre = dummy
        current = head
        while current:
            if current.val == val:
                pre.next = current.next
            else:
                pre = pre.next
            current = current.next
        return dummy.next

if __name__ == '__main__':
    s = Solution()
    print(listnode_to_list(s.removeElements(create_listnode([1, 2, 6, 3, 4, 5, 6]), 6)))
    print(listnode_to_list(s.removeElements(create_listnode([6,1, 2, 6, 3, 4, 5]), 6)))
