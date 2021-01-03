class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def create_listnode(nums: list):
    dummy = ListNode(None)
    current = dummy
    for _, num in enumerate(nums):
        current.next = ListNode(num)
        current = current.next
    return dummy.next
def listnode_to_list(head:ListNode):
    result=[]
    while head:
        result.append(head.val)
        head=head.next
    return result