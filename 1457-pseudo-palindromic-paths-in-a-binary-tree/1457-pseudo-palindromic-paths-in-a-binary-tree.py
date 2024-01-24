# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def isPalindrome(arr):
            odd_count = 0
            for count in arr.values():
                if count % 2 != 0:
                    odd_count += 1
                    if odd_count > 1:
                        return False
            return True

        def traverse(root, path):
            if root:
                path[root.val] += 1

                if not root.left and not root.right:  # leaf node
                    nonlocal res
                    if isPalindrome(path):
                        res += 1
                else:
                    traverse(root.left, path)
                    traverse(root.right, path)

                path[root.val] -= 1

        res = 0
        path = Counter()
        traverse(root, path)
        return res