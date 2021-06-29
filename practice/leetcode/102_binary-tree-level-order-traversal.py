# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        level = [root]
        res = []
        while level:
            res.append([node.val for node in level])
            level = sum([[node.left, node.right] for node in level], [])
            level = [node for node in level if node if not None]

        return res
