"""
有两个属性：val和next。val是当前节点的值，next是指向下一个节点的指针/引用。
如果要使用双向链表，则还需要一个属性prev以指示链表中的上一个节点。假设链表中的所有节点都是 0-index 的。

在链表类中实现这些功能：

get(index)：获取链表中第index个节点的值。如果索引无效，则返回-1。
addAtHead(val)：在链表的第一个元素之前添加一个值为val的节点。插入后，新节点将成为链表的第一个节点。
addAtTail(val)：将值为val 的节点追加到链表的最后一个元素。
addAtIndex(index,val)：在链表中的第index个节点之前添加值为val 的节点。如果index等于链表的长度，则该节点将附加到链表的末尾。如果 index 大于链表长度，则不会插入节点。如果index小于0，则在头部插入节点。
deleteAtIndex(index)：如果索引index 有效，则删除链表中的第index 个节点。

示例：
MyLinkedList linkedList = new MyLinkedList();
linkedList.addAtHead(1);
linkedList.addAtTail(3);
linkedList.addAtIndex(1,2);   //链表变为1-> 2-> 3
linkedList.get(1);            //返回2
linkedList.deleteAtIndex(1);  //现在链表是1-> 3
linkedList.get(1);            //返回3

提示：
所有val值都在[1, 1000]之内。
操作次数将在[1, 1000]之内。
请不要使用内置的 LinkedList 库。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/design-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from ListNodeHelper import ListNode, create_listnode, listnode_to_list


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dummy = ListNode(None)

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        current = self.dummy.next
        counter = 0
        while current:
            if counter == index:
                return current.val
            current = current.next
            counter += 1
        return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        bef_head = self.dummy.next
        self.dummy.next = ListNode(val)
        self.dummy.next.next = bef_head

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        pre=self.dummy
        current = self.dummy.next
        while current:
            current = current.next
            pre=pre.next
        pre.next = ListNode(val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        pre = self.dummy
        current = self.dummy.next
        counter = 0
        while current:
            if counter == index:
                pre.next = ListNode(val)
                pre.next.next = current
                break
            current = current.next
            pre = pre.next
            counter += 1
        if not current and counter==index:
            pre.next=ListNode(val)

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        pre = self.dummy
        current = self.dummy.next
        counter = 0
        while current:
            if counter == index:
                pre.next = current.next
                break
            pre = pre.next
            current = current.next
            counter += 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
if __name__ == '__main__':
    s = MyLinkedList()
    # s.addAtHead(1)
    # s.addAtTail(3)
    # s.addAtIndex(1, 2)
    # print(listnode_to_list(s.dummy.next))
    # print(s.get(1))
    # s.deleteAtIndex(1)
    # print(listnode_to_list(s.dummy.next))
    # print(s.get(1))

    # s.addAtHead(7)
    # s.addAtHead(2)
    # s.addAtHead(1)
    # print(listnode_to_list(s.dummy.next))
    # s.addAtIndex(3,0)
    # print(listnode_to_list(s.dummy.next))

    s.addAtTail(1)
    print(s.get(1))

