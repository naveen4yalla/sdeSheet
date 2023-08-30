class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def is_unique(sub):
            # Check if all characters in sub are unique
            return len(sub) == len(set(sub))

        def backtrack(index, current):
            nonlocal max_length

            # Check if the current subsequence has unique characters
            if is_unique(current):
                max_length = max(max_length, len(current))

            # Explore all possible subsequences
            for i in range(index, len(arr)):
                # Include the current string in the subsequence
                backtrack(i + 1, current + arr[i])

        max_length = 0
        backtrack(0, "")
        return max_length
