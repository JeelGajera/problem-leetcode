# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def traversal(root):
            res = []
            if root:
                res += traversal(root.left)
                if root.left is None and root.right is None:
                    res.append(root.val)
                res += traversal(root.right)
            return res
            
        return traversal(root1) == traversal(root2)