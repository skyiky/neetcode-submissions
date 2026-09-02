# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return []

        q = deque()
        q.append(root)
        while q:
            last = None
            size = len(q)
            for i in range(size):
                n = q.popleft()
                last = n.val
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            result.append(last)
        return result
            
            
            

        