"""
给定一个单链表，随机选择链表的一个节点，并返回相应的节点值。保证每个节点被选的概率一样。
进阶:
如果链表十分大且长度未知，如何解决这个问题？你能否使用常数级空间复杂度实现？
示例:

// 初始化一个单链表 [1,2,3].
ListNode head = new ListNode(1);
head.next = new ListNode(2);
head.next.next = new ListNode(3);
Solution solution = new Solution(head);

// getRandom()方法应随机返回1,2,3中的一个，保证每个元素被返回的概率相等。
solution.getRandom();

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/linked-list-random-node
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for singly-linked list.
import random


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.arr = []
        while head:
            self.arr.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        return random.choice(self.arr)


# 蓄水池抽样算法
import random


class Solution:

    def __init__(self, head: ListNode):
        self.head = head

    def getRandom(self) -> int:
        """
        最近经常能看到面经中出现在大数据流中的随机抽样问题

即：当内存无法加载全部数据时，如何从包含未知大小的数据流中随机选取k个数据，并且要保证每个数据被抽取到的概率相等。

当 k = 1 时，即此题的情况
也就是说，我们每次只能读一个数据。

假设数据流含有N个数，我们知道如果要保证所有的数被抽到的概率相等，那么每个数抽到的概率应该为 1/N

那如何保证呢？

先说方案：

每次只保留一个数，当遇到第 i 个数时，以 1/i的概率保留它，(i-1)/i的概率保留原来的数。

举例说明： 1 - 10

遇到1，概率为1，保留第一个数。
遇到2，概率为1/2，这个时候，1和2各1/2的概率被保留
遇到3，3被保留的概率为1/3，(之前剩下的数假设1被保留)，2/3的概率 1 被保留，(此时1被保留的总概率为 2/3 * 1/2 = 1/3)
遇到4，4被保留的概率为1/4，(之前剩下的数假设1被保留)，3/4的概率 1 被保留，(此时1被保留的总概率为 3/4 * 2/3 * 1/2 = 1/4)
以此类推，每个数被保留的概率都是1/N。

        """
        count = 0
        reserve = 0
        cur = self.head
        while cur:
            count += 1
            rand = random.randint(1, count)
            if rand == count:
                reserve = cur.val
            cur = cur.next
        return reserve
