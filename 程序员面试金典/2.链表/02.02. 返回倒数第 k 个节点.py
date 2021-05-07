"""
实现一种算法，找出单向链表中倒数第 k 个节点。返回该节点的值。

注意：本题相对原题稍作改动

示例：

输入： 1->2->3->4->5 和 k = 2
输出： 4
说明：

给定的 k保证是有效的。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/kth-node-from-end-of-list-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from ListNodeHelper import ListNode, create_listnode


class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        rtn_node = head
        for i in range(k):
            head = head.next
        while head:
            head = head.next
            rtn_node = rtn_node.next
        return rtn_node.val


if __name__ == '__main__':
    s = Solution()
    print(s.kthToLast(create_listnode([1, 2, 3, 4, 5]), 5))
