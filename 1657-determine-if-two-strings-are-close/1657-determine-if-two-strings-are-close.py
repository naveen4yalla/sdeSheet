from collections import Counter
class Solution:
    def closeStrings(self,word1: str, word2: str) -> bool:
        freq1 = Counter(word1)
        freq2 = Counter(word2)

        # Check if the character frequencies are the same
        if freq1.keys() == freq2.keys():
            # Check if the sorted frequency values are the same
            return sorted(freq1.values()) == sorted(freq2.values())

        return False


        