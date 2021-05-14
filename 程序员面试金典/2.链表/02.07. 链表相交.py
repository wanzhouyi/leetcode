"""
给定两个（单向）链表，判定它们是否相交并返回交点。请注意相交的定义基于节点的引用，而不是基于节点的值。换句话说，如果一个链表的第k个节点与另一个链表的第j个节点是同一节点（引用完全相同），则这两个链表相交。

示例 1：
输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
输出：Reference of the node with value = 8
输入解释：相交节点的值为 8 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。
示例 2：
输入：intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
输出：Reference of the node with value = 2
输入解释：相交节点的值为 2 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [0,9,1,2,4]，链表 B 为 [3,2,4]。在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。

示例 3：

输入：intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
输出：null
输入解释：从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。由于这两个链表不相交，所以 intersectVal 必须为 0，而 skipA 和 skipB 可以是任意值。
解释：这两个链表不相交，因此返回 null。

注意：

如果两个链表没有交点，返回 null 。
在返回结果后，两个链表仍须保持原有的结构。
可假定整个链表结构中没有循环。
程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/intersection-of-two-linked-lists-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from ListNodeHelper import ListNode, create_listnode


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        暴力法，注意使用set，比较快
        """
        nodes_A = set()
        while headA:
            nodes_A.add(headA)
            headA = headA.next
        while headB:
            if headB in nodes_A:
                return headB
            headB = headB.next

        return None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        这题应该是比较明显的双指针题，要是能实现一种算法让两个指针分别从A和B点往C点走，两个指针分别走到C后，又各自从另外一个指针的起点，也就是A指针第二次走从B点开始走，B指针同理，这样，A指针走的路径长度 AO + OC + BO 必定等于B指针走的路径长度 BO + OC + AO，这也就意味着这两个指针第二轮走必定会在O点相遇，相遇后也即到达了退出循环的条件，代码如下：
        作者：ceamanz
        链接：https://leetcode-cn.com/problems/intersection-of-two-linked-lists-lcci/solution/shuang-zhi-zhen-zou-liang-bian-zou-dao-di-er-bian-/
        来源：力扣（LeetCode）
        著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        """
        ta, tb = headA, headB
        while ta != tb:
            ta = ta.next if ta else headB
            tb = tb.next if tb else headA
        return tb


if __name__ == '__main__':
    s = Solution()
    print(s.getIntersectionNode(create_listnode([4, 1, 8, 4, 5]),
                                create_listnode([5, 0, 1, 8, 4, 5])))
