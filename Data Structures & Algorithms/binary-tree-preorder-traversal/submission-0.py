# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        result = []

        def dfs(node):
            if node is None:
                return 0

            result.append(node.val)    

            dfs(node.left)
            dfs(node.right)

            return result
        return dfs(root)
            

        