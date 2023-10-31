class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        res = [pref[0]]
        if len(pref) > 1:
            a = pref[0] ^ pref[1]
            res.append(a)
        for i in range(1,len(pref)-1):
            tmp = pref[i] ^ pref[i+1]
            res.append(tmp)
        return res