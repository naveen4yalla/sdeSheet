class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        prefixSum = [0]
        result = 0
        for f in range(len(nums)):
            prefixSum.append(prefixSum[-1] + nums[f])
        monoStack = []
        for i, value in enumerate(nums):
            # to know where to start the subsequence
            newIndex = i
            while monoStack and monoStack[-1][1] > value:
                tempi, v = monoStack.pop()
                total = prefixSum[i] - prefixSum[tempi]
                result = max(result, v * total)
                newIndex = tempi
            monoStack.append([newIndex, value])
        for i, val in monoStack:
            total = prefixSum[len(nums)] - prefixSum[i]
            result = max(result, val * total)
        return result % (10**9 + 7)