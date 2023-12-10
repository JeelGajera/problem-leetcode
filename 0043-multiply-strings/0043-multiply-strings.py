class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        l1,l2 = len(num1), len(num2)
        result = [0]*(l1+l2)

        for i in range(l1-1,-1,-1):
            carry = 0
            for j in range(l2-1,-1,-1):
                temp = (ord(num1[i]) - ord("0"))*(ord(num2[j]) - ord("0")) + result[i+j+1] + carry
                result[i+j+1] = temp % 10
                carry = temp // 10

            result[i] += carry

        result_str = "".join(map(str, result))
        return result_str.lstrip("0") or "0"