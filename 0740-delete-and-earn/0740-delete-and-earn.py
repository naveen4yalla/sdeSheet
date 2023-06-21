# class Solution:
#     def deleteAndEarn(self, nums: List[int]) -> int:
# #         points = defaultdict(int)
# #         max_number = 0
# #         # Precompute how many points we gain from taking an element
# #         for num in nums:
# #             points[num] += num
# #             max_number = max(max_number, num)

# #         @cache
# #         def max_points(num):
# #             # Check for base cases
# #             if num == 0:
# #                 return 0
# #             if num == 1:
# #                 return points[1]
            
# #             # Apply recurrence relation
# #             return max(max_points(num - 1), max_points(num - 2) + points[num])
        
# #         return max_points(max_number)
from collections import defaultdict

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = defaultdict(int)
        max_number = 0
        
        # Precompute how many points we gain from taking an element
        for num in nums:
            points[num] += num
            max_number = max(max_number, num)
        
        two_back = 0
        one_back = points.get(1, 0)
        
        for num in range(2, max_number + 1):
            two_back, one_back = one_back, max(one_back, two_back + points.get(num, 0))

        return one_back