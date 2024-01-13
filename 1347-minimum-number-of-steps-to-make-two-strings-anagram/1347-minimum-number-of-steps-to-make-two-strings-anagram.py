class Solution:
    def minSteps(self, s: str, t: str) -> int:
        f1 = defaultdict(int)
        f2 = defaultdict(int)
        res = 0
        n = len(s)

        for i in range(n):
            f1[s[i]] += 1
            f2[t[i]] += 1

        for i in set(t):
            diff = f2[i] - f1.get(i, 0)
            if diff > 0:
                res += diff

        return res