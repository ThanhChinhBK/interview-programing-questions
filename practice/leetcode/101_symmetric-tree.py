# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        root.right = self.reverseTree(root.right)
        return self.isSameTree(root.left, root.right)
        
    def reverseTree(self, root):
        if root is None:
            return root
        root.left, root.right = root.right, root.left
        root.left = self.reverseTree(root.left)
        root.right = self.reverseTree(root.right)
        return root
    
    def isSameTree(self, root1, root2):
        if root1 == None and root2 == None:
            return True
        elif root1 == None or root2 == None:
            return False
        return root1.val == root2.val and self.isSameTree(root1.left, root2.left) and self.isSameTree(root1.right, root2.right)
