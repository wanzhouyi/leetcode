"""
判断一个链表是否为回文链表。

示例 1:

输入: 1->2
输出: false
示例 2:

输入: 1->2->2->1
输出: true
"""

from .ListNodeHelper import ListNode


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        from collections import deque
        dq = deque()
        while head:
            dq.append(head.val)
            head = head.next
        while len(dq) > 1:
            left = dq.popleft()
            right = dq.pop()
            if left != right:
                return False
        return True
