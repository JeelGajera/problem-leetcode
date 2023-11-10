class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        tab = {"{":"}", "(":")", "[":"]", "}":"", "]":"", ")":""}
        for i in s:
            if len(stack) == 0:
                stack.append(i)
            elif tab[stack[-1]] == i:
                stack.pop()
            else:
                stack.append(i)
        return True if len(stack) == 0 else False
        