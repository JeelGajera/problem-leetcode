class Solution:
    def sortVowels(self, s: str) -> str:
        res = []
        idx = []

        for i in range(len(s)):
            if s[i].lower() in ['a', 'e', 'i', 'o', 'u']:
                idx.append(i)
                res.append(ord(s[i]))

        res.sort()
        tmp = list(s)

        for i in range(len(res)):
            tmp[idx[i]] = chr(res[i])
        
        str_sort = "".join(tmp)
        
        return str_sort