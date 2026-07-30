class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        for i in range(len(prices)-1, -1, -1):
            if len(stack) == 0:
                stack.append(prices[i])
                continue
            curr = prices[i]

            while stack and curr < stack[-1]:
                stack.pop()

            if stack:
                prices[i] = curr - stack[-1]

            stack.append(curr)
            
        return prices