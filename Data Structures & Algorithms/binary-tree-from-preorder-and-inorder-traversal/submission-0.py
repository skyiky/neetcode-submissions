# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = { v: i for i, v in enumerate(inorder) }
        preorder_index = 0

        # Builds and returns the subtree containing exactly the nodes in inorder[l:r+1]
        def dfs(l, r) -> Optional[TreeNode]:
            nonlocal preorder_index

            if l > r:
                return None
            
            node_value = preorder[preorder_index]
            preorder_index += 1

            node = TreeNode(node_value)
            node_inorder_index = inorder_map[node_value]
            
            node.left = dfs(l, node_inorder_index - 1)
            node.right = dfs(node_inorder_index + 1, r)

            return node

        return dfs(0, len(inorder) - 1)



        