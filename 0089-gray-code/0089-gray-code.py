class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return [0]

        gray_code = [0, 1]

        for i in range(1, n):
            size = len(gray_code)
            
            for j in range(size - 1, -1, -1):
                gray_code.append((1 << i) | gray_code[j])

        return gray_code