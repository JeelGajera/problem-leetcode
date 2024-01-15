class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = set()
        losers = set()
        loser_player = Counter()

        for match in matches:
            winner, loser = match
            winners.add(winner)
            losers.add(loser)
            loser_player[loser] += 1

        res1 = list(winners-losers)
        res2 = [player for player, count in loser_player.items() if count == 1]
        return [sorted(res1), sorted(res2)]