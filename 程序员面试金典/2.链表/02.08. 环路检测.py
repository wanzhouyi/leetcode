"""
给定一个链表，如果它是有环链表，实现一个算法返回环路的开头节点。
如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。

示例 1：
输入：head = [3,2,0,-4], pos = 1
输出：tail connects to node index 1
解释：链表中有一个环，其尾部连接到第二个节点。

示例 2：
输入：head = [1,2], pos = 0
输出：tail connects to node index 0
解释：链表中有一个环，其尾部连接到第一个节点。

示例 3：
输入：head = [1], pos = -1
输出：no cycle
解释：链表中没有环。

进阶：

你是否可以不用额外空间解决此题？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/linked-list-cycle-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from ListNodeHelper import ListNode


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        """暴力法，记得使用set
        一个非常直观的思路是：我们遍历链表中的每个节点，并将它记录下来；
        一旦遇到了此前遍历过的节点，就可以判定链表中存在环。借助哈希表可以很方便地实现。
        """
        nodes = set()
        while head:
            if head in nodes:
                return head
            nodes.add(head)
            head = head.next
        return None

    def detectCycle(self, head: ListNode) -> ListNode:
        """快慢指针
        使用两个指针，fast 与slow。它们起始都位于链表的头部。
        随后，slow 指针每次向后移动一个位置，而 fast 指针向后移动两个位置。
        如果链表中存在环，则fast 指针最终将再次与 slow 指针在环中相遇。

        如下图所示，设链表中环外部分的长度为 a。slow 指针进入环后，又走了 b 的距离与 fast 相遇。
        此时，fast 指针已经走完了环的 n 圈，因此它走过的总距离为a+n(b+c)+b=a+(n+1)b+nc。

        根据题意，任意时刻，fast 指针走过的距离都为 slow 指针的 2 倍。因此，我们有

        a+(n+1)b+nc=2(a+b)⟹a=c+(n−1)(b+c)

        有了 a=c+(n-1)(b+c)a=c+(n−1)(b+c) 的等量关系，我们会发现：从相遇点到入环点的距离加上 n−1 圈的环长，
        恰好等于从链表头部到入环点的距离。

        因此，当发现 slow 与 fast 相遇时，我们再额外使用一个指针 ptr。起始，它指向链表头部；
        随后，它和 slow 每次向后移动一个位置。最终，它们会在入环点相遇。

        作者：LeetCode-Solution
        链接：https://leetcode-cn.com/problems/linked-list-cycle-lcci/solution/huan-lu-jian-ce-by-leetcode-solution-s2la/
        来源：力扣（LeetCode）
        著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

        """
        slow, fast = head, head
        while fast and fast.next:  # 开始走位
            slow = slow.next
            fast = fast.next.next
            if slow == fast:  # 相遇
                break

        # 若无相会处，则无环路
        if not fast or not fast.next:
            return None
        # 若两者以相同的速度移动，则必然在环路起始处相遇
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
