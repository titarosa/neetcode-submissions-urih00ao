# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(p, q):
            if not p and not q:
                return True # If we traverse both tree completely is true
            
            if not p or not q: # If onr tree is emoty and not the other is false
                return False

            if q.val != p.val: #checking if values matching
                return False

            return dfs(p.left, q.left) and dfs(p.right, q.right) #traverse both tree to the left
        return dfs(p,q)
     
         

            

  



        