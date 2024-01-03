class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        rows = []
        res = 0
        for i in bank:
            ones = i.count("1")
            if ones > 0:
                rows.append(ones)

        for i in range(len(rows)-1):
            res += rows[i]*rows[i+1]
            
        return res