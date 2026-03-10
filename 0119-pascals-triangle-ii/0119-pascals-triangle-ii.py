class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        prev = [1]
        curr = []
        for j in range(rowIndex+1):
            for i in range(j+1):
                x = 1
                if i > 0 and i < j:
                    x = prev[i-1] + prev[i]
                curr.append(x)
            prev = curr
            curr = []
        return prev