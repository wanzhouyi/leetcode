"""
编写程序以 x 为基准分割链表，使得所有小于 x 的节点排在大于或等于 x 的节点之前。
如果链表中包含 x，x 只需出现在小于 x 的元素之后(如下所示)。分割元素 x 只需处于“右半部分”即可，
其不需要被置于左右两部分之间。

示例:

输入: head = 3->5->8->5->10->2->1, x = 5
输出: 3->1->2->10->5->5->8

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/partition-list-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from ListNodeHelper import ListNode, listnode_to_list, create_listnode


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        """
        方法一，暴力法
        """
        root1, root2, root3 = ListNode(0), ListNode(0), ListNode(0)
        head1, head2, head3 = root1, root2, root3
        while head:
            if head.val < x:
                head1.next = head
                head1 = head1.next
            elif head.val > x:
                head2.next = head
                head2 = head2.next
            elif head.val == x:
                head3.next = head
                head3 = head3.next
            head = head.next
        if root2.next:
            head1.next = root2.next
            head2.next = root3.next
        else:
            head1.next = root3.next
        head3.next = None
        return root1.next if root1.next else root3.next


if __name__ == '__main__':
    s = Solution()
    print(listnode_to_list(s.partition(create_listnode([1, 4, 3, 2, 5, 2]), 3)))
    print(listnode_to_list(s.partition(create_listnode([1]), 0)))
    print(listnode_to_list(s.partition(create_listnode([1]), 3)))
    print(listnode_to_list(s.partition(create_listnode([1]), 1)))
    print(listnode_to_list(s.partition(create_listnode([1, 2]), 2)))
