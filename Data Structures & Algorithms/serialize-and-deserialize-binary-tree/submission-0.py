# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        result = []
        
        def dfs(node) -> None:
            if not node:
                result.append("N")
                return
            
            result.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return ",".join(result)

    # Decodes your encoded data to tree.
    # Deserialize recursively consumes the preorder list:
    # N     → return None
    # value → create node, build left subtree, then right subtree
    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = data.split(",")
        i = 0

        def dfs() -> Optional[TreeNode]:
            nonlocal i
            d = values[i]
            i += 1
            if d == "N":
                return None
            node = TreeNode(int(d))
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()