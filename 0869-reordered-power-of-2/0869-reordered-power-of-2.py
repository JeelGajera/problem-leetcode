class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def count(num):
            return Counter(str(num))

        sorted_n = sorted(str(n))

        for i in range(30):
            power_2 = 1 << i
            sorted_power_2 = sorted(str(power_2))
            if count(n) == count(power_2) and sorted_n == sorted_power_2:
                return True

        return False