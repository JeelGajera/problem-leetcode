class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        max_cnt = -1
        position = {}

        for i, char in enumerate(s):
            if char in position:
                max_cnt = max(max_cnt, i - position[char] - 1)
            else:
                position[char] = i

        return max_cnt