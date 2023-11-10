class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generateValidParentheses(s, left, right, n):
            if len(s) == 2 * n:
                result.append(s)
                return
            if left < n:
                generateValidParentheses(s + '(', left + 1, right, n)
            if right < left:
                generateValidParentheses(s + ')', left, right + 1, n)

        result = []
        generateValidParentheses('', 0, 0, n)
        return result