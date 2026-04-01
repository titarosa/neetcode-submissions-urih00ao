# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if root is None:
            return []

        nodeVal = []

        def dfs(root):
            if not root:
                return 

            dfs(root.left)
            dfs(root.right)
            nodeVal.append(root.val)

            return nodeVal

        return dfs(root)
    




        