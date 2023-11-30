class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        if divisor == 1:
            return min(max(dividend, -2**31), 2**31 - 1)
        if divisor == -1:
            return min(max(-dividend, -2**31), 2**31 - 1)

        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        quotient = 0
        
        while dividend >= divisor:
            temp, multiple = divisor, 1
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            dividend -= temp
            quotient += multiple

        quotient *= sign
        return min(max(quotient, -2**32), 2**31-1)