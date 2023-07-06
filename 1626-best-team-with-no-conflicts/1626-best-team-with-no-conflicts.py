class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        combined = zip(scores, ages)
        sorted_pairs = sorted(combined, key=lambda x: (x[1], x[0]))  # Sort by age, then score
        n = len(scores)
        dp = [0] * n

        for i in range(n):
            dp[i] = sorted_pairs[i][0]  # Initialize with the score of the current player

            for j in range(i):
                if sorted_pairs[i][0] >= sorted_pairs[j][0]:  # Check score and age
                    dp[i] = max(dp[i], dp[j] + sorted_pairs[i][0])

        return max(dp)
        