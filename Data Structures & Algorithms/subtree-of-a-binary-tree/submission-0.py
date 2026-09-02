# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    # dfs(node, subRoot) returns True when the tree rooted at subRoot appears anywhere 
    # inside the tree rooted at root
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        if self.isEqual(root, subRoot):
            return True
        return (
            self.isSubtree(root.left, subRoot)
            or self.isSubtree(root.right, subRoot)
        )
        
    # dfs(a, b) returns True when the trees rooted at a and b are identical
    def isEqual(self, a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
        if not a and not b:
            return True
        if not a or not b or a.val != b.val:
            return False
        return (
            self.isEqual(a.left, b.left)
            and self.isEqual(a.right, b.right)
        )
        