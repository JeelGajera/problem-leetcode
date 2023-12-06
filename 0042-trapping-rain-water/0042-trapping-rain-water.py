class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l, r = [0]*n, [0]*n
        l[0], r[-1] = height[0], height[-1]
        res = 0
        for i in range(1,n):
            l[i] = max(l[i-1], height[i])
        for i in range(n-2,-1,-1):
            r[i] = max(r[i+1], height[i])
        for i in range(n):
            res += min(l[i],r[i]) - height[i]
        return res