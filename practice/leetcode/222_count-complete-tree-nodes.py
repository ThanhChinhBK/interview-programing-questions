import math

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        def get_depth(root):
            if root is None:
                return 0
            return 1 + get_depth(root.left)
        right_depth = get_depth(root.right)
        left_depth = get_depth(root.left)
        if right_depth == left_depth:
            return int(math.pow(2, left_depth) + self.countNodes(root.right))
        else:
            return int(math.pow(2, right_depth) + self.countNodes(root.left))
