class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        while n > 1:
            count = 1
            tmp = []
            for i in range(len(s)-1):
                if s[i] == s[i+1]:
                    count += 1
                else:
                    tmp.append(str(count) + s[i])
                    count = 1
            tmp.append(str(count) + s[-1])
            s = "".join(tmp)
            n -= 1
        return s