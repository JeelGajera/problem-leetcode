class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ['+', '-', '*', "/"]
        stack = []
        for token in tokens:
            if token not in ops:
                stack.append(token)
            else:
                i2 = int(stack.pop())
                i1 = int(stack.pop())
                res = 0
                if token == '+':
                    res = i1 + i2
                elif token == '-':
                    res = i1 - i2
                elif token == '*':
                    res = i1 * i2
                elif token == '/':
                    res = int(i1 / i2)

                stack.append(res)

        return int(stack.pop())