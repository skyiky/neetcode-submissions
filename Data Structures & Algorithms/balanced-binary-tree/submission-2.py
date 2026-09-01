# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # dfs(node) returns:
        # (True, height)  if the subtree is balanced
        # (False, height) if the subtree is unbalanced
        def dfs(root: Optional[TreeNode]) -> tuple[bool, int]:
            if root is None:
                return True, 0
            lbal, lh = dfs(root.left)
            rbal, rh = dfs(root.right)

            balanced = (
                lbal
                and rbal
                and abs(lh - rh) <= 1
            )

            return (balanced, max(lh, rh) + 1)
        
        return dfs(root)[0]
    