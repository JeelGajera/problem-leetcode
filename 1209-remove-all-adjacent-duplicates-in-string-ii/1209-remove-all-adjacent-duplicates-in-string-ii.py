class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        arr = list(s)
        stack = []

        for char in arr:
            if stack and stack[-1][0] == char:
                stack[-1][1] += 1
            else:
                stack.append([char, 1])

            if stack[-1][1] == k:
                stack.pop()
        
        print(stack)
        result = ''.join(char * count for char, count in stack)
        return result