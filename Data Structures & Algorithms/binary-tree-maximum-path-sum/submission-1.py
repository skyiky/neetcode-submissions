# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = float('-inf') # <-- Always need a global variable, if 'local subtree' answers matter!

        def dfs(node) -> int:
            nonlocal result

            if not node:
                return 0

            lsum = dfs(node.left)
            rsum = dfs(node.right)

            # best complete path whose highest point is node
            best_complete_path = max(
                lsum + node.val,
                node.val,
                rsum + node.val,
                lsum + node.val + rsum,
            )
            result = max(result, best_complete_path)
            
            # best non-branching path that can be returned to the parent
            best_extendable_path = max(
                lsum + node.val,
                node.val,
                rsum + node.val,
            )
            return best_extendable_path 

        dfs(root)
        return result











