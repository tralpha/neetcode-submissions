# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        output = []
        # PRE-ORDER N MARK
        def build(node):
            if node == None:
                output.append('N')
                return
            output.append(str(node.val))
            build(node.left)
            build(node.right)
        build(root)
        # JOIN
        return ",".join(s for s in output)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # ITER CONSUME
        strs = iter(data.split(","))
        def funcs():
            s = next(strs)
            if s == 'N':
                return None
            node = TreeNode(val=s)
            # RECURSE LR
            node.left = funcs()
            node.right = funcs()
            return node
        return funcs()
