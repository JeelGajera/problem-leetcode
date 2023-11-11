class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.graph = defaultdict(list)
        for from_node, to_node, cost in edges:
            self.graph[from_node].append((to_node, cost))
        self.n = n
        
    def addEdge(self, edge: List[int]) -> None:
        from_node, to_node, cost = edge
        self.graph[from_node].append((to_node, cost))

    def shortestPath(self, node1: int, node2: int) -> int:
        dist = [float('inf')] * self.n
        dist[node1] = 0

        pq = [(0, node1)]

        while pq:
            current_dist, current_node = heapq.heappop(pq)

            if current_node == node2:
                return dist[node2]

            if current_dist > dist[current_node]:
                continue

            for neighbor, edge_cost in self.graph[current_node]:
                new_dist = dist[current_node] + edge_cost
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))
        return -1


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)