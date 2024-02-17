import heapq

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        for i in range(1, len(heights)):
            gap = heights[i] - heights[i-1]
            if gap > 0:
                heapq.heappush(heap, gap)
                if len(heap) > ladders:
                    # heap pop returns the smallest gap
                    bricks -= heapq.heappop(heap) 
                    
                # no more possible jumps
                if bricks < 0:
                    return i-1

        return len(heights)-1

