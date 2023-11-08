class Solution:
    def reverseWords(self, s: str) -> str:
        str_list = [x for x in s.split(" ") if x != '']
        str_list = str_list[::-1]
        res = " ".join(str_list)
        return res