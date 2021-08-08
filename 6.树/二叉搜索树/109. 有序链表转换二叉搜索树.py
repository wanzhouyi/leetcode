"""
给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。
本题中，一个高度平衡二叉树是指一个二叉树每个节点的左右两个子树的高度差的绝对值不超过 1。
示例:
给定的有序链表： [-10, -3, 0, 5, 9],
一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：
      0
     / \
   -3   9
   /   /
 -10  5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        values = []
        while head:
            values.append(head.val)
            head = head.next

        def build_tree(nums: list):
            if not nums:
                return None
            mid = len(nums) // 2
            node = TreeNode(nums[mid])
            node.left = build_tree(nums[:mid])
            node.right = build_tree(nums[mid + 1:])
            return node

        root = build_tree(values)
        return root


# 官解
# 前言
# 将给定的有序链表转换为二叉搜索树的第一步是确定根节点。由于我们需要构造出平衡的二叉树，
# 因此比较直观的想法是让根节点左子树中的节点个数与右子树中的节点个数尽可能接近。
# 这样一来，左右子树的高度也会非常接近，可以达到高度差绝对值不超过 1 的题目要求。
# 如何找出这样的一个根节点呢？我们可以找出链表元素的中位数作为根节点的值。
#
# 这里对于中位数的定义为：如果链表中的元素个数为奇数，那么唯一的中间值为中位数；
# 如果元素个数为偶数，那么唯二的中间值都可以作为中位数，而不是常规定义中二者的平均值。
#
# 根据中位数的性质，链表中小于中位数的元素个数与大于中位数的元素个数要么相等，要么相差 1。
# 此时，小于中位数的元素组成了左子树，大于中位数的元素组成了右子树，它们分别对应着有序链表中连续的一段。
# 在这之后，我们使用分治的思想，继续递归地对左右子树进行构造，找出对应的中位数作为根节点，以此类推。
#
# 可以证明，这样的构造方法得到的二叉搜索树是平衡的，详见文末的「正确性证明」部分。
#
# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree/solution/you-xu-lian-biao-zhuan-huan-er-cha-sou-suo-shu-1-3/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class Solution:
    """
    方法一：分治
    我们可以直接模拟「前言」部分的构造方案。
    具体地，设当前链表的左端点为 left，右端点right，包含关系为「左闭右开」，即left 包含在链表中而 right不包含在链表中。
    我们希望快速地找出链表的中位数节点mid。

    为什么要设定「左闭右开」的关系？由于题目中给定的链表为单向链表，访问后继元素十分容易，但无法直接访问前驱元素。
    因此在找出链表的中位数节点mid 之后，如果设定「左闭右开」的关系，
    我们就可以直接用 (left,mid) 以及 (mid.next,right) 来表示左右子树对应的列表了。
    并且，初始的列表也可以用 (head,null) 方便地进行表示，其中 null 表示空节点。

    找出链表中位数节点的方法多种多样，其中较为简单的一种是「快慢指针法」。
    初始时，快指针 fast 和慢指针 slow 均指向链表的左端点left。我们将快指针 fast 向右移动两次的同时，
    将慢指针 slow 向右移动一次，直到快指针到达边界（即快指针到达右端点或快指针的下一个节点是右端点）。
    此时，慢指针对应的元素就是中位数。

    在找出了中位数节点之后，我们将其作为当前根节点的元素，并递归地构造其左侧部分的链表对应的左子树，
    以及右侧部分的链表对应的右子树。

    作者：LeetCode-Solution
    链接：https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree/solution/you-xu-lian-biao-zhuan-huan-er-cha-sou-suo-shu-1-3/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def getMedian(left: ListNode, right: ListNode) -> ListNode:
            fast = slow = left
            while fast != right and fast.next != right:
                fast = fast.next.next
                slow = slow.next
            return slow

        def buildTree(left: ListNode, right: ListNode) -> TreeNode:
            if left == right:
                return None
            mid = getMedian(left, right)
            root = TreeNode(mid.val)
            root.left = buildTree(left, mid)
            root.right = buildTree(mid.next, right)
            return root

        return buildTree(head, None)


if __name__ == '__main__':
    s = Solution()


    def create_listnode(nums: list):
        dummy = ListNode(None)
        current = dummy
        for _, num in enumerate(nums):
            current.next = ListNode(num)
            current = current.next
        return dummy.next


    s.sortedListToBST(create_listnode([-10, -3, 0, 5, 9]))
