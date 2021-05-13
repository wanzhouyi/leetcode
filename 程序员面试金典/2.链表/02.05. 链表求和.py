"""
给定两个用链表表示的整数，每个节点包含一个数位。
这些数位是反向存放的，也就是个位排在链表首部。
编写函数对这两个整数求和，并用链表形式返回结果。

示例：

输入：(7 -> 1 -> 6) + (5 -> 9 -> 2)，即617 + 295
输出：2 -> 1 -> 9，即912
进阶：思考一下，假设这些数位是正向存放的，又该如何解决呢?

示例：
输入：(6 -> 1 -> 7) + (2 -> 9 -> 5)，即617 + 295
输出：9 -> 1 -> 2，即912

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sum-lists-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from ListNodeHelper import ListNode


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        双指针解法
        """
        root = ListNode(0)
        head = root
        jinwei = 0
        while l1 and l2:
            val = l1.val + l2.val + jinwei
            if val > 9:
                jinwei = 1
                val -= 10
            else:
                jinwei = 0

            head.next = ListNode(val)
            head = head.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            val = l1.val + jinwei
            if val > 9:
                jinwei = 1
                val -= 10
            else:
                jinwei = 0

            head.next = ListNode(val)
            head = head.next
            l1 = l1.next

        while l2:
            val = l2.val + jinwei
            if val > 9:
                jinwei = 1
                val -= 10
            else:
                jinwei = 0

            head.next = ListNode(val)
            head = head.next
            l2 = l2.next

        if jinwei > 0:
            head.next = ListNode(jinwei)
        return root.next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """双指针解法，代码好看版本"""
        head = ListNode(0)
        node = head
        remaining = 0
        while l1 or l2:
            if l1 == None:
                node.next = l2
                l1 = ListNode(0)
            if l2 == None:
                node.next = l1
                l2 = ListNode(0)
            remaining += l1.val + l2.val
            node.next = ListNode(remaining % 10)
            remaining = remaining // 10
            node = node.next
            l1 = l1.next
            l2 = l2.next
        if remaining:
            node.next = ListNode(remaining)
        return head.next


if __name__ == '__main__':
    s = Solution()
    print(s.addTwoNumbers())
