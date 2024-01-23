class Solution:
    def maxLength(self, arr: List[str]) -> int:
        char_set = set()
        def overlap(char_set, s):
            prev = set()
            for c in s:
                if c in char_set or c in prev:
                    return True
                prev.add(c)
            return False

        def backtrack(i):
            if i == len(arr):
                return len(char_set)

            res = 0
            if not overlap(char_set, arr[i]):
                for c in arr[i]:
                    char_set.add(c)
                res = max(res, backtrack(i+1))
                for c in arr[i]:
                    char_set.remove(c)
            
            return max(res, backtrack(i+1))

        return backtrack(0)
