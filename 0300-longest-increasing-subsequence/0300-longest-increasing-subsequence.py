class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        sub = []

        def binary_search(sub, val):
            lo, hi = 0, len(sub)-1
            while lo <= hi:
                mid = lo + (hi-lo)//2
                if sub[mid] < val:
                    lo = mid + 1
                elif sub[mid] > val:
                    hi = mid - 1
                else:
                    return mid
            return lo

        for x in nums:
            i = binary_search(sub, x)
            if i == len(sub):
                sub.append(x)
            else:
                sub[i] = x
                
        return len(sub)