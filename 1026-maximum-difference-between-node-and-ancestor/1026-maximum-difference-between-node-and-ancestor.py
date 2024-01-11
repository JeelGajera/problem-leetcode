# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        max_diff = 0
        def traversTree(root, low, high):
            nonlocal max_diff
            if root:
                max_diff = max(max_diff, abs(root.val - low), abs(root.val - high))
                l, h = min(root.val, low), max(root.val, high)
                traversTree(root.left,l,h)
                traversTree(root.right,l,h)

        traversTree(root, root.val, root.val)
        return max_diff
