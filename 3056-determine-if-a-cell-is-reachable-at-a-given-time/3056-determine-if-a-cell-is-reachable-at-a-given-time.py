class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if sx == fx and sy == fy and t == 1:
            return False
        tmp = max(abs(fx-sx), abs(fy-sy))
        if tmp <= t:
            return  True
        return False