class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        MOD = 10**9 + 7
        stack = []
        left = [0] * n
        right = [0] * n

        for i in range(n):
            while stack and arr[i] < arr[stack[-1]]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        stack = []

        for i in range(n - 1, -1, -1):
            while stack and arr[i] <= arr[stack[-1]]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)

        result = 0

        for i in range(n):
            result += arr[i] * (i - left[i]) * (right[i] - i)
            result %= MOD

        return result