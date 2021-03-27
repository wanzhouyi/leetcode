"""
给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动k个位置。
示例 1：
输入：head = [1,2,3,4,5], k = 2
输出：[4,5,1,2,3]
示例 2：
输入：head = [0,1,2], k = 4
输出：[2,0,1]
提示：

链表中节点的数目在范围 [0, 500] 内
-100 <= Node.val <= 100
0 <= k <= 2 * 109

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rotate-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from ListNodeHelper import *


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head

        root = ListNode(0)
        root.next = head

        # 计算链表长度
        length = 0
        end = None
        while head:
            end = head
            head = head.next
            length += 1
        # 计算真实需要倒转的节点
        rotate_length = k % length
        cnt = 0
        head = root.next
        while cnt < length - 1 - rotate_length:
            head = head.next
            cnt += 1

        if head != end:
            temp = root.next
            root.next = head.next
            head.next = None
            end.next = temp
        return root.next


if __name__ == '__main__':
    s = Solution()
    print(listnode_to_list(s.rotateRight(create_listnode([1, 2, 3, 4, 5]), 2)))
