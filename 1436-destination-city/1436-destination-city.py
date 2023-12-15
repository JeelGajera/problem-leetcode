class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        route = {}
        n = len(paths)
        for i in range(n):
            route[paths[i][0]] = paths[i][1]

        source = list(route.keys())
        city = source[0]
        while city in source:
            city = route[city]
        else:
            return city
