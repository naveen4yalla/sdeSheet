from functools import lru_cache
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        #optimise the performance
        nums.sort()
        
        @lru_cache(maxsize = None)
        def combinations(remain):
            if remain == 0:
                return 1
            result = 0
            for num in nums:
                if remain - num >= 0:
                    result += combinations(remain - num)
                else:
                    break
            return result 
        return combinations(target)
            