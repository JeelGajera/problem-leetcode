class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        n = len(tokens)
        if n == 1:
            return int(tokens[0])
    
        operators = ['+', '-', '*', '/']
        stack = []

        for i in range(n):
            if tokens[i] in operators:
                op2 = stack.pop()
                op1 = stack.pop()
                res = int(eval(str(op1)+tokens[i]+str(op2)))
                stack.append(res)
            else:
                stack.append(tokens[i])

        return stack[0]