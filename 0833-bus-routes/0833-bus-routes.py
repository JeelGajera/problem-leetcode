class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        stops_map = defaultdict(set)
        if source == target:
            return 0

        for i, route in enumerate(routes):
            for stop in route:
                stops_map[stop].add(i)

        queue = deque([(source, 0)])
        visited = set([source])

        while queue:
            cur_stop, bus_count = queue.popleft()
            if cur_stop == target:
                return bus_count

            for bus in stops_map[cur_stop]:
                for next_stop in routes[bus]:
                    if next_stop not in visited:
                        queue.append((next_stop, bus_count + 1))
                        visited.add(next_stop)
                routes[bus] = []

        return -1