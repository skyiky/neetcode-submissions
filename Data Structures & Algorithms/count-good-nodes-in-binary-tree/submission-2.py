# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def goodNodes(node: TreeNode, path_max: int) -> int:
            if not node:
                return 0
    
            count = 1 if node.val >= path_max else 0
            path_max = max(node.val, path_max)

            return (
                count
                + goodNodes(node.left, path_max)
                + goodNodes(node.right, path_max)
            )

        return goodNodes(root, root.val)
        