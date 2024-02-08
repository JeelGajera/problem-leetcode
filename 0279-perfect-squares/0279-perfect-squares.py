import math

class Solution:
    def numSquares(self, n: int) -> int:
        def is_perfect_square(num):
            return int(math.sqrt(num))**2 == num

        def num_squares(n):
            # n it self is square
            if is_perfect_square(n):
                return 1
            
            # if n can be represent by sum of 2
            for i in range(1, int(math.sqrt(n)) + 1):
                if is_perfect_square(n - i*i):
                    return 2
                    
            # if n can be represent by sum of 4
            while n % 4 == 0:
                n //= 4
            if n % 8 == 7:
                return 4

            # only option left now number must be represent by 3
            return 3

        return num_squares(n)
