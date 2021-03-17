"""
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
说明:
1 ≤m≤n≤ 链表长度。

示例:

输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-linked-list-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        root = ListNode(0)  # 定义哨兵节点
        root.next = head
        cnt = 1  # 定义计数器
        pre = root  # 定义前缀指针
        while head.next:
            # 如果是在left部分,直接指针后移
            if cnt < left:
                pre = head
                head = head.next
                cnt += 1
            # 如果是界于left和right之间,则翻转
            elif left <= cnt < right:
                nxt = head.next
                head.next = nxt.next
                nxt.next = pre.next
                pre.next = nxt
                cnt += 1
            else:
                break
        return root.next


if __name__ == '__main__':
    s = Solution()
    root = head = ListNode()
    for i in range(1, 6):
        node = ListNode(i)
        head.next = node
        head = head.next
    # new= s.reverseBetween(root.next,2,4)
    new = s.reverseBetween(root.next, 1, 5)
