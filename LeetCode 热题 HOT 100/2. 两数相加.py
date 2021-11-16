"""
给你两个非空 的链表，表示两个非负的整数。它们每位数字都是按照逆序的方式存储的，并且每个节点只能存储一位数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0开头。



示例 1：


输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.
示例 2：

输入：l1 = [0], l2 = [0]
输出：[0]
示例 3：

输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]


提示：

每个链表中的节点数在范围 [1, 100] 内
0 <= Node.val <= 9
题目数据保证列表表示的数字不含前导零

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        jinwei = 0
        stack = []
        while l1 and l2:
            temp_sum = l1.val + l2.val + jinwei
            jinwei = 0
            if temp_sum > 9:
                jinwei = 1
                temp_sum -= 10
            stack.append(ListNode(temp_sum))
            l1 = l1.next
            l2 = l2.next
        while l1:
            temp_sum = l1.val + jinwei
            jinwei = 0
            if temp_sum > 9:
                jinwei = 1
                temp_sum -= 10
            stack.append(ListNode(temp_sum))
            l1 = l1.next

        while l2:
            temp_sum = l2.val + jinwei
            jinwei = 0
            if temp_sum > 9:
                jinwei = 1
                temp_sum -= 10
            stack.append(ListNode(temp_sum))
            l2 = l2.next

        if jinwei > 0:
            stack.append(ListNode(jinwei))

        head = node = ListNode(0)
        while stack:
            node.next = stack.pop(0)
            node = node.next
        return head.next
