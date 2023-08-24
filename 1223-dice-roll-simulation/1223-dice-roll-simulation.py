class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        mod = 10**9 + 7

        def func(index, prevNumber, prevNumberFrequency):
            if index == n:
                return 1
            if (index, prevNumber, prevNumberFrequency) in dp:
                return dp[(index, prevNumber, prevNumberFrequency)]
            ans = 0
            for i in range(1, 7):
                if i == prevNumber:
                    if prevNumberFrequency < rollMax[i - 1]:
                        ans = (ans + func(index + 1, prevNumber, prevNumberFrequency + 1)) % mod
                else:
                    ans = (ans + func(index + 1, i, 1)) % mod
            dp[(index, prevNumber, prevNumberFrequency)] = ans
            return ans

        dp = {}
        return func(0, 0, 0)
