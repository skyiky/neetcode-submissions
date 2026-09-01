# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # dfs(node):
        # 1. returns whether the tree rooted at node is balanced
        # 2. returns the height of node's subtree
        def dfs(root: Optional[TreeNode]) -> (bool, int):
            if root is None:
                return (True, 0)
            lbal, lh = dfs(root.left)
            rbal, rh = dfs(root.right)
            if not lbal or not rbal or abs(lh - rh) > 1:
                return (False, -1)
            return (True, max(lh, rh) + 1)
        
        return dfs(root)[0]
    