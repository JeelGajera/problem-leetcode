class Solution:
    def numberOfWays(self, corridor: str) -> int:
        if corridor.count("S") < 2 or corridor.count("S") % 2 != 0:
            return 0
        else:
            count = 1
            MOD = 10**9 + 7
            seats = 0
            prev_seat = 0
            for i in range(len(corridor)):
                if corridor[i] == 'S':
                    seats += 1
                    if seats % 2 == 0:
                        prev_seat = i
                    elif seats > 1:
                        count *= (i - prev_seat)
            return count % MOD