class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        res = [0]*n

        for i in range(n-1,-1,-1):
            curr = temperatures[i]

            while stack and stack[-1][0] <= curr:
                stack.pop()

            if len(stack) == 0:
                res[i] = (0, None)
            else:
                res[i] = stack[-1]

            stack.append((curr, i))

        for i in range(n):
            if res[i][1] is None:
                res[i] = 0
            else:
                res[i] = res[i][1] - i

        return res