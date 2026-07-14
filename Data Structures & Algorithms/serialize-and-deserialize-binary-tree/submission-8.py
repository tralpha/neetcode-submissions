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
        # PREORDER N MARK
        def dfs(node):
            if node == None:
                output.append('N')
                return
            output.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        # JOIN
        return ",".join(c for c in output)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # ITER CONSUME
        tokens = iter(data.split(","))
        def build():
            c = next(tokens)
            if c == 'N':
                return None
            node = TreeNode(val=int(c))
            # RECURSE LR
            node.left = build()
            node.right = build()
            return node
        return build()
        
