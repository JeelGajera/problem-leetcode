class Solution:
    def isPathCrossing(self, path: str) -> bool:
        points = set()
        point = (0,0)
        points.add(point)

        for i in path:
            if i == "N":
                point = (point[0], point[1]+1)
            elif i == "E":
                point = (point[0]+1, point[1])
            elif i == "S":
                point = (point[0], point[1]-1)
            elif i == "W":
                point = (point[0]-1, point[1])

            if point in points:
                return True
                
            points.add(point)
            
        return False