from bisect import bisect_right

class Solution(object):
    def longestObstacleCourseAtEachPosition(self, obstacles):
        n = len(obstacles)
        dp = [0] * n
        lis = []
        for i in range(n):
            idx = bisect_right(lis, obstacles[i])
            if idx == len(lis):
                lis.append(obstacles[i])
            else:
                lis[idx] = obstacles[i]
            dp[i] = idx + 1
        return dp