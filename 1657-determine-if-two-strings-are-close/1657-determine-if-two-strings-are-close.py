class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        f1 = Counter(word1)
        f2 = Counter(word2)
        char1 = set(word1)
        char2 = set(word2)
        return (char1 == char2) and (sorted(f1.values()) == sorted(f2.values()))