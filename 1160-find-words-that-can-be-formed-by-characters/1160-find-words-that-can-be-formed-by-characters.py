class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_count = Counter(chars)
        result = 0

        for word in words:
            word_count = Counter(word)

            if all(word_count[char] <= char_count[char] for char in word):
                result += len(word)

        return result