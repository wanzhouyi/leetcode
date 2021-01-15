"""
给你一个链表数组，每个链表都已经按升序排列。
请你将所有链表合并到一个升序链表中，返回合并后的链表。

示例 1：

输入：lists = [[1,4,5],[1,3,4],[2,6]]
输出：[1,1,2,3,4,4,5,6]
解释：链表数组如下：
[
  1->4->5,
  1->3->4,
  2->6
]
将它们合并到一个有序链表中得到。
1->1->2->3->4->4->5->6

示例 2：

输入：lists = []
输出：[]

示例 3：

输入：lists = [[]]
输出：[]

提示：

k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] 按 升序 排列
lists[i].length 的总和不超过 10^4


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-k-sorted-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for singly-linked list.
from heapq import heappop
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists or len(lists) == 0:
            return None
        import heapq
        heap = []
        # 首先 for 嵌套 while 就是将所有元素都取出放入堆中
        for node in lists:
            while node:
                heapq.heappush(heap, node.val)
                node = node.next
        dummy = ListNode(None)
        cur = dummy
        # 依次将堆中的元素取出(因为是小顶堆，所以每次出来的都是目前堆中值最小的元素），然后重新构建一个列表返回
        while heap:
            temp_node = ListNode(heappop(heap))
            cur.next = temp_node
            cur = temp_node
        return dummy.next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        n = len(lists)
        if n == 1:
            return lists[0]
        elif n == 2:
            return self.merge(lists[0], lists[1])
        else:
            mid = n // 2
            return self.merge(self.mergeKLists(lists[:mid]),
                              self.mergeKLists(lists[mid:]))

    def merge(self, node1: ListNode, node2: ListNode):
        ptr1, ptr2 = node1, node2
        dummy = ListNode()
        current = dummy
        while ptr1 and ptr2:
            if ptr1.val < ptr2.val:
                current.next = ptr1
                ptr1 = ptr1.next
            else:
                current.next = ptr2
                ptr2 = ptr2.next
            current = current.next
        if ptr1:
            current.next = ptr1
        if ptr2:
            current.next = ptr2
        return dummy.next
