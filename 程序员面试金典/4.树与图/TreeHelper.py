# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def create_tree(arr: str):
    # [4,2,5,1,3,null,6,0]
    arr = list(map(lambda x: int(x) if x != 'null' else None, arr.strip('[]').split(',')))
    if not arr:
        return None
    root = TreeNode(arr.pop(0))
    stack = [root]
    while arr:
        node = stack.pop(0)
        val = arr.pop(0)
        if val is not None:
            node.left = TreeNode(val)
            stack.append(node.left)
        else:
            node.left = None

        if arr:
            val = arr.pop(0)
            if val is not None:
                node.right = TreeNode(val)
                stack.append(node.right)
            else:
                node.right = None
    return root
