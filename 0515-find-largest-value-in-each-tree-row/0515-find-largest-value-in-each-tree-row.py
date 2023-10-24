# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        q = deque()
        q.append(root)
        if not root:
            return res
        while q:
            level = len(q)
            maxi = float('-inf')
            for i in range(level):
                tmp = q.popleft()
                if tmp.left:
                    q.append(tmp.left)
                if tmp.right:
                    q.append(tmp.right)
                maxi = max(maxi, tmp.val)
            res.append(maxi)
        return res