class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        for i in range(len(candidates)):
            if candidates[i] > target:
                candidates = candidates[0:i]
                break
        
        def backtrack(start, target, path):
            if target == 0:
                res.append(path)
                return
            for i in range(start, len(candidates)):
                if candidates[i] <= target:
                    backtrack(i, target - candidates[i], path + [candidates[i]])

        backtrack(0,target, [])
        return res