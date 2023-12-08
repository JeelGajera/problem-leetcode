# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        left_str = self.tree2str(root.left)
        right_str = self.tree2str(root.right)

        result = str(root.val)

        if left_str or right_str:
            result += f'({left_str})'

        if right_str:
            result += f'({right_str})'

        return result