"""
存在一个按升序排列的链表，给你这个链表的头节点 head ，请你删除链表中所有存在数字重复情况的节点，
只保留原始链表中没有重复出现的数字。返回同样按升序排列的结果链表。

示例 1：
输入：head = [1,2,3,3,4,4,5]
输出：[1,2,5]

示例 2：
输入：head = [1,1,1,2,3]
输出：[2,3]

提示：

链表中节点数目在范围 [0, 300] 内
-100 <= Node.val <= 100
题目数据保证链表已经按升序排列

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from ListNodeHelper import create_listnode, ListNode, listnode_to_list


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        root = ListNode(0)
        root.next = head
        pre = root
        while head and head.next:
            if head.next and head.val != head.next.val:
                pre = head
                head = head.next
            else:
                while head.next and head.val == head.next.val:
                    head = head.next
                head = head.next
                pre.next = head
        return root.next


if __name__ == '__main__':
    s = Solution()
    print(listnode_to_list(s.deleteDuplicates(create_listnode([1, 2, 3, 3, 4, 4, 5]))))
    print(listnode_to_list(s.deleteDuplicates(create_listnode([1, 1, 1, 2, 3]))))
