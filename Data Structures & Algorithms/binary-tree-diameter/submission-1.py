# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        # recursive contract of dfs(node):
        # 1. returns the height of node's subtree
        # 2. updates 'diameter' with the largest diameter encountered
        def dfs(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0
            
            l = dfs(root.left)
            r = dfs(root.right)

            nonlocal diameter
            diameter = max(diameter, l + r)

            return max(l, r) + 1 # child's height + current node
        
        dfs(root)

        return diameter
