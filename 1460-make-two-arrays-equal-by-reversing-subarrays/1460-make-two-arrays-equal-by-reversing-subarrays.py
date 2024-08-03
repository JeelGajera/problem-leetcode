class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        if arr == target:
            return True
        else:
            arr.sort()
            target.sort()
            return arr == target