# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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


def tree_to_arr(root: TreeNode):
    pass


create_tree("[4,2,5,1,3,null,6,0]")
