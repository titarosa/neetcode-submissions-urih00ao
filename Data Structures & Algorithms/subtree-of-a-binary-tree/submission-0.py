# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def subTree(tree1, tree2):
            if tree1 is None and tree2 is None:
                return True
            if tree1 is None and tree2 is not None:
                return False
            if tree1 is not None and tree2 is None:
                return False
            return (tree1.val == tree2.val and subTree(tree1.left, tree2.left) and subTree(tree1.right, tree2.right))

        if root is None:
            return False
        
        if subTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot) 



        


        