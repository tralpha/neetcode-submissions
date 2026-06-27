# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # PREORDER-N-MARK
        out = []
        def dfs(node):
            if node == None:
                out.append('N')
                return
            out.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        # JOIN
        return ','.join(out)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # ITER-CONSUME
        tokens = iter(data.split(','))
        def build():
            v = next(tokens)
            if v == 'N':
                return None
            node = TreeNode(int(v))
            # RECURSE LR
            node.left = build()
            node.right = build()
            return node
        return build()

        
