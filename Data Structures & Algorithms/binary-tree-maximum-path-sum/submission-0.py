# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = float('-inf')

        def dfs(node) -> int:
            nonlocal result

            if not node:
                return 0

            lsum = dfs(node.left)
            rsum = dfs(node.right)

            localresult = max(
                lsum + node.val,
                node.val,
                rsum + node.val,
                lsum + node.val + rsum,
            )
            result = max(result, localresult)

            pathresult = max(
                lsum + node.val,
                node.val,
                rsum + node.val,
            )
            # return largest path that includes node:
            # l,n | n | r,n
            return pathresult

        dfs(root)
        return result











