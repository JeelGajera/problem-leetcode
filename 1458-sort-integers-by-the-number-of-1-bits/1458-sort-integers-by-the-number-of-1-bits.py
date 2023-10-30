class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        # return sorted(arr, key=lambda x: (bin(x).count('1'),x))
        arr.sort()
        for i in range(1,len(arr)):
            while bin(arr[i-1]).count("1") > bin(arr[i]).count("1") and i > 0:
                arr[i-1], arr[i] = arr[i], arr[i-1]
                i -= 1
        return arr
