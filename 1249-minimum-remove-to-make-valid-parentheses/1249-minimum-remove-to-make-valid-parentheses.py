class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        stack = []
        for i,v in enumerate(s):
            if v == "(":
                stack.append(i)
            elif v == ")":
                if stack:
                    stack.pop()
                else:
                    s[i] = ""
        
        while stack:
            s[stack.pop()] = ""

        return "".join(s)

