"""
反转一个单链表。
示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from ListNodeHelper import ListNode, create_listnode, listnode_to_list


class Solution:
    # 方法一，打散法，32ms
    def reverseList(self, head: ListNode) -> ListNode:
        dummy=ListNode(None)
        stack=[]
        while head:
            stack.append(head)
            head=head.next
        current=dummy
        while stack:
            current.next=stack.pop()
            current=current.next
        current.next=None
        return dummy.next
    # 方法二，原地反转，40ms
    def reverseList(self, head: ListNode) -> ListNode:
        dummy=ListNode(None)
        dummy.next=head
        while head and head.next:
            nxt=head.next
            head.next=nxt.next
            nxt.next=dummy.next
            dummy.next=nxt
        return dummy.next





if __name__ == '__main__':
    s = Solution()
    print(listnode_to_list(s.reverseList(create_listnode([1,2,3,4,5]))))
    # 空链表
    print(listnode_to_list(s.reverseList(create_listnode([]))))
    # 单节点链表
    print(listnode_to_list(s.reverseList(create_listnode([1]))))
