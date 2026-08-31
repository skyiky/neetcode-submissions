# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Depth(node)
#     = 1 + max(
#         depth(left),
#         depth(right)
#       )
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
# 1. Define the recursive contract
#       "dfs(node) returns ______ for the tree rooted at node."
# 2. Trust the child calls
#       Think:
#       Parent node
#           receives completed left answer
#           receives completed right answer
#           combines them
# 3. Combine child results
# 4. Find the empty tree answer
#       "What should the function return when node does not exist?"
# 5. Verify The Contract
