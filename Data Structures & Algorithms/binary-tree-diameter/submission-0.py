# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        # recursive contract
        # dfs(node) returns the max depth starting from node
        def dfs(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0
            
            l = dfs(root.left) 
            r = dfs(root.right)

            nonlocal res
            res = max(res, l + r)

            return max(l, r) + 1
        
        dfs(root)

        return res
