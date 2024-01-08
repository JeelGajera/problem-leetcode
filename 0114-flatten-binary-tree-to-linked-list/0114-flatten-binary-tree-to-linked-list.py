# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def traverse(root):
            if root:
                rtmp = root.right
                ltmp = root.left

                # pre-order traversel
                traverse(ltmp)
                traverse(rtmp)

                root.right = ltmp
                root.left = None

                current = root
                while current.right:
                    current = current.right

                current.right = rtmp

        traverse(root)
            
        