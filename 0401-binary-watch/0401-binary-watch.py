class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        res = []
        for hr in range(12):
            for mi in range(60):
                if bin(hr).count("1") + bin(mi).count("1") == turnedOn:
                    res.append(f"{hr}:{mi:02d}")
        return res