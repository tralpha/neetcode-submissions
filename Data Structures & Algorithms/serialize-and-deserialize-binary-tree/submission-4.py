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
        def dfs(root):
            # PRE-ORDER N MARK
            if root == None:
                output.append('N')
                return
            output.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        # JOIN
        return ",".join(s for s in output)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # ITER CONSUME
        tokens = iter(data.split(","))
        def build():
            token = next(tokens)
            if token == 'N':
                return None
            node = TreeNode(val=int(token))
            # RECURSE LR
            node.left = build()
            node.right = build()
            return node
        return build()
        
