class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        if right:
            min_right = n - min(right)
        else:
            min_right = 0
        if left:
            min_left = max(left)
        else:
            min_left = 0
        return max(min_right, min_left)