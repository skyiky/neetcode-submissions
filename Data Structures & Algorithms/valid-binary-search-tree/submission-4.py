# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # bottom up dfs: Information moves children → parent.
    # def dfs(node):
    #   if not node:
    #       return EMPTY_SUMMARY

    #   left_summary = dfs(node.left)
    #   right_summary = dfs(node.right)

    #   return combine(
    #     node,
    #     left_summary,
    #     right_summary,
    #   )
    #
    # top down dfs: Information moves parent → child.
    # def dfs(node, context):
    #   if not node:
    #       return BASE_RESULT
    #
    #   if not valid(node, context):
    #       return FAILURE
    #
    #   left_context = update_for_left(context, node)
    #   right_context = update_for_right(context, node)
    #
    #   return (
    #       dfs(node.left, left_context)
    #       and dfs(node.right, right_context)
    #   )
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # for tree rooted at node, returns the smallest and largest value in the tree and if the tree is a valid BST
        # def dfs(node: Optional[TreeNode]) -> tuple[bool, float, float]:
        #     if not node:
        #         return (True, float('inf'), float('-inf'))
        #
        #     lvalid, lmin, lmax = dfs(node.left)
        #     rvalid, rmin, rmax = dfs(node.right)
        #     if lvalid and rvalid and lmax < node.val < rmin:
        #         return (True, min(lmin, node.val), max(rmax, node.val))
        #     else:
        #         return (False, float('-inf'), float('inf'))
        # return dfs(root)[0]
        #
        def valid(node, lower, upper) -> bool:
            if not node:
                return True

            if not lower < node.val < upper:
                return False

            return (
                valid(node.left, lower, node.val)
                and valid(node.right, node.val, upper)
            )

        return valid(root, float('-inf'), float('inf'))

        