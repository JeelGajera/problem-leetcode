class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        i = 1 
        arr = []
        oprationarray= []
        idx = 0

        while i <= n and len(arr) !=len(target): 
            arr.append(i)
            oprationarray.append("Push")
            if(arr[idx]!=target[idx]) :
                arr.pop()
                oprationarray.append("Pop")
                idx-=1
            
            idx+=1
            i+=1
        return oprationarray
