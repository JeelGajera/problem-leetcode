# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def travers_bt(root, res):
            if root:
                travers_bt(root.left, res)
                res.append(root.val)
                travers_bt(root.right, res)
                
        res = []
        travers_bt(root, res)
        return res