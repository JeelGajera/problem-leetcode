# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    import collections

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def traverse_BST(root):
            if root is None:
                return []
            list1 = []
            list1 += traverse_BST(root.left)
            list1.append(root.val)
            list1 += traverse_BST(root.right)
            return list1

        res = traverse_BST(root)
        # get mode
        mode_dict = {}
        max_value = 0

        for element in res:
            if element in mode_dict:
                mode_dict[element] += 1
            else:
                mode_dict[element] = 1

        for key, value in mode_dict.items():
            if value > max_value:
                max_value = value

        if max_value == 1:
            return res
        else:
            return [key for key, value in mode_dict.items() if value == max_value]