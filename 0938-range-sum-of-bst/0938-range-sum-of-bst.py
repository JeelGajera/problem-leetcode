# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        def traverseBST(root):
            if root:
                res = 0
                if low <= root.val <= high:
                    res += root.val

                if root.val > low:
                    res += traverseBST(root.left)

                if root.val < high:
                    res += traverseBST(root.right)

                return res
            else:
                return 0

        total = traverseBST(root)
        return total 