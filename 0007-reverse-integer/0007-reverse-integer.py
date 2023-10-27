class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        is_negative = False
        if x < 0:
            is_negative = True
            x = -x

        # Reverse the integer
        reversed_x = 0
        while x > 0:
            reversed_x = reversed_x * 10 + x % 10
            x //= 10

        # Check for overflow
        if is_negative:
            reversed_x = -reversed_x

        if reversed_x > 2**31 - 1 or reversed_x < -2**31:
            return 0 

        return reversed_x