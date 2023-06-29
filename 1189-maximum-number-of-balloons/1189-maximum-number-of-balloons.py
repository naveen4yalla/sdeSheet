# class Solution:
#     def maxNumberOfBalloons(self, text: str) -> int:
#         counter = collections.Counter(text)
#         counter['l'] //= 2
#         counter['o'] //= 2
#         return min(counter[c] for c in 'balon')
from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        ls = Counter(text)
        inputText = "balloon"
        count = 0
        i = 0
        while True:
            if i >= len(inputText):
                i = 0
            if inputText[i] not in ls or ls[inputText[i]] == 0:
                return count // len(inputText)
            ls[inputText[i]] -= 1
            i += 1
            count += 1
