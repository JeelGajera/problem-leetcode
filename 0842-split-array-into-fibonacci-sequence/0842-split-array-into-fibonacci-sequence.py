class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        max_int = 2**31 - 1
        arr = []
        
        def backtrack(cur, arr, num):
            if cur == len(num) and len(arr) >= 3:
                return arr
            for i in range(cur, len(num)):
                if num[cur] == '0' and i > cur:
                    break  # leading 0 not allowed
                x = int(num[cur:i + 1])
                if x > max_int:
                    break  # check for out of bounds
                if len(arr) <= 1 or x == arr[-1] + arr[-2]:
                    arr.append(x)
                    nxt = backtrack(i + 1, arr, num)
                    if nxt:
                        return nxt
                    arr.pop()

            return []

        return backtrack(0, arr, num)