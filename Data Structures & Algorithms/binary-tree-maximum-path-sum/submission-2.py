# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        best = [float('-inf')]
        def dfs(node):
            if node == None:
                return 0
            # DFS GAIN
            # CLIP NEG
            L = max(0, dfs(node.left))
            R = max(0, dfs(node.right))
            # UPDATE THROUGH
            through = node.val + L + R
            best[0] = max(best[0], through)
            # RETURN SINGLE SIDE
            return node.val + max(L, R)
        dfs(root)
        return best[0]