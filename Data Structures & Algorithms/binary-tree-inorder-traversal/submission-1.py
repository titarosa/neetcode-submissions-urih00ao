# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if root is None:
            return []

        result = []

        def dfs(node):
            if node is None:
                return []
            
            dfs(node.left)
            result.append(node.val)
            dfs(node.right)

            return result
        return dfs(root)
        