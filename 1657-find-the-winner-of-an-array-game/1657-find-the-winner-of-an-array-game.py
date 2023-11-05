class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k>=len(arr)-1:return max(arr)
        d=defaultdict(lambda:0)
        while d[arr[0]]<k:
            arr.append(arr.pop(1 if arr[0]>arr[1] else 0))
            d[arr[0]]+=1
        return  max(d.keys(),key= lambda x:d[x])