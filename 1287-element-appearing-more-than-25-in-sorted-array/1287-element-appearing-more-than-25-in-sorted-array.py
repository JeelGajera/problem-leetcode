class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        l = len(arr)
        res = 0
        for i in arr:
            if (arr.count(i)/l)*100 > 25:
                res = i
        return res