class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        seed = 1

        while seed < 10:
            current = seed
            next_digit = seed + 1

            while current <= high and next_digit < 10:
                current = current * 10 + next_digit

                if low <= current <= high:
                    res.append(current)

                next_digit += 1

            seed += 1

        return sorted(res)