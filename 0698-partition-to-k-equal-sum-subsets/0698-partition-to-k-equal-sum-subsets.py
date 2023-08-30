# class Solution:
#     def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
#         nums.sort(reverse=True)
#         total = sum(nums) / k
#         visited = set()
        

#         def backTrack(i, count, value):
#             if k == count:
#                 return True
#             if value == total:
#                 return backTrack(0, count + 1, 0)
#             for j in range(i, len(nums)):
#                 if j != 0 and (j-1) not in visited and nums[j - 1] == nums[j]:
#                     continue
#                 if j in visited or nums[j] + value > total:
#                     continue
#                 visited.add(j)
#                 if backTrack(j + 1, k, value + nums[j]):
#                     return True
#                 visited.remove(j)
#             return False

#         return backTrack(0, 0, 0)
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        nums.sort(reverse=True)
        total = sum(nums) / k
        visited = set()

        def backTrack(i, count, value):
            if count == k:
                return True
            if value == total:
                return backTrack(0, count + 1, 0)
            for j in range(i, len(nums)):
                if j != i and nums[j - 1] == nums[j] and j - 1 not in visited:
                    continue
                if j in visited or nums[j] + value > total:
                    continue
                visited.add(j)
                if backTrack(j + 1, count, value + nums[j]):
                    return True
                visited.remove(j)
            return False

        return backTrack(0, 0, 0)
