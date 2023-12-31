class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12 or len(s) < 4:
            return []
        
        res = []

        def backtrack(i, dots, ip):
            if dots == 4 and i == len(s):
                res.append(ip[:-1])
                return

            if dots > 4:
                return 

            for k in range(i, min(i+3, len(s))):
                if int(s[i:k+1]) < 256 and (k==i or s[i] != "0"):
                    backtrack(k+1, dots+1, ip + s[i:k+1] + ".")

        backtrack(0,0,"")
        
        return res