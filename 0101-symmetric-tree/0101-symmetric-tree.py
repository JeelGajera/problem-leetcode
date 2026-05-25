# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def helper(left: TreeNode, right: TreeNode):
            if(left == None or right == None):
                return left == right
            return left.val == right.val and helper(left.left, right.right) and helper(left.right, right.left)
        if(root == None):
            return true
        return helper(root.left, root.right)
        