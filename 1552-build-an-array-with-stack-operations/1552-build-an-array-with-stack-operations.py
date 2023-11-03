from collections import deque

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack = []
        res = []
        for i in range(1,n+1):
            if stack != target:
                stack.append(i)
                res.append("Push")
                if i not in target:
                    rm = stack.pop()
                    res.append("Pop")
        return res

        