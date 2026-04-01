# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        # root = [1,2,3], targetSum = 3
        def dfs(node, curr_sum):
            if node is None:
                return False # Step 1: No, Step 2: No

            curr_sum += node.val #  Step 1: 1,  Step 2: 3

            if not node.left and not node.right:
                return curr_sum == targetSum #Step 1: False, Step 2: True - Done

            return dfs(node.left, curr_sum) or  dfs(node.right, curr_sum) # dfs(2,1)
     

        return dfs(root, 0)
        

            









        