class Solution:
    def maxProduct(self, s: str) -> int:
        def is_palindrome(subsequence):
            return subsequence == subsequence[::-1]
        max_product = 0
        palindromes = {}
        n = len(s)

        # Generate all possible subsequences
        for i in range(1, 2 ** n):
            subsequence = ''
            for j in range(n):
                if (i >> j) & 1:
                    subsequence += s[j]
            if is_palindrome(subsequence):
                length = len(subsequence)
                palindromes[i] = length
        for i in palindromes:
            for j in palindromes:
                if i & j == 0:
                    max_product = max(palindromes[i]*palindromes[j],max_product)
        return max_product



        # Find two disjoint subsequences with maximum product of lengths
       