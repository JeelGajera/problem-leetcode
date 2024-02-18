import heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        res = [0]*n
        meetings.sort(key=lambda x: x[0])
        available_room = [r for r in range(n)]
        rooms = []
        heapify(available_room)
        
        for s,e in meetings:
            while rooms and rooms[0][0] <= s:
                t,r = heappop(rooms)
                heappush(available_room, r)
            
            if available_room:
                r = heappop(available_room)
                heappush(rooms, [e, r])
            else:
                t,r = heappop(rooms)
                heappush(rooms, [t+e-s, r])
            
            res[r] += 1

        return res.index(max(res))