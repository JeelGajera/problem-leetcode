class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        node_score = defaultdict(int)

        for j, edge in enumerate(edges):
            node_score[edge] += j
            
        max_score = max(node_score.values())
        max_score_nodes = [node for node, score in node_score.items() if score == max_score]
        return min(max_score_nodes)