# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:

        def convertBSTtoGraph(root, graph):
            if root:
                if root.left:
                    graph[root.val].append(root.left.val)
                    graph[root.left.val].append(root.val)
                    convertBSTtoGraph(root.left, graph)

                if root.right:
                    graph[root.val].append(root.right.val)
                    graph[root.right.val].append(root.val)
                    convertBSTtoGraph(root.right, graph)

        def bfs(graph, start):
            visited = set()

            queue = deque([(start, 0)])
            visited.add(start)

            max_distance = 0

            while queue:
                current, dist = queue.popleft()

                for neighbor in graph[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, dist + 1))

                        if dist + 1 > max_distance:
                            max_distance = dist + 1

            return max_distance
        
        graph = defaultdict(list)
        convertBSTtoGraph(root, graph)

        return bfs(graph, start)