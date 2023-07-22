#Top Down Dynamic Programming
# class Solution:
#     def splitArray(self, nums, k) -> int:
#         def dp(start, k):
#             if k == 1:
#                 return sum(nums[start:])
#             if (start, k) in memo:
#                 return memo[(start, k)]

#             max_sum = float('inf')
#             subarray_sum = 0
#             for i in range(start, len(nums) - k + 1):
#                 subarray_sum += nums[i]
#                 max_sum = min(max_sum, max(subarray_sum, dp(i + 1, k - 1)))

#             memo[(start, k)] = max_sum
#             return max_sum

#         memo = {}
#         return dp(0, k)
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def canSplit(largest):
            subarray = 0
            curSum = 0
            for n in nums:
                curSum += n
                if curSum > largest:
                    subarray += 1
                    curSum = n
            return subarray + 1 <= m

        l, r = max(nums), sum(nums)
        res = r
        while l <= r:
            mid = l + ((r - l) // 2)
            if canSplit(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res
