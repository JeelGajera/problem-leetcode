# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        height = 0

        def dfs(root, cur_h):
            nonlocal height
            if root:
                height = max(height, cur_h)
                dfs(root.left, cur_h+1)
                dfs(root.right, cur_h+1)

        dfs(root, 1)
        return height
                