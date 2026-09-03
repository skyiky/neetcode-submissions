# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # in-order traversal
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # The counter belongs to the whole traversal, not one subtree. Therefore, all recursive calls must share it.
        # "Does this value summarize one subtree, or track progress across all subtrees?"
        visited = 0
        answer = 0

        # dfs(node) processes node’s subtree in sorted order.   
        #           It returns True if the kth node is found; otherwise, it returns False.
        def dfs(node):
            nonlocal visited, answer
            if not node: # base case
                return False

            if dfs(node.left): # traverse left, if returned True, early break
                return True

            visited += 1 # process root
            if visited == k: # check if root is answer
                answer = node.val
                return True

            return dfs(node.right) # traverse right

        dfs(root)
        return answer
