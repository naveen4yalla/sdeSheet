# class Solution:
#     def longestOnes(self, nums, k):
#         left = 0 
#         result = 0
#         for right in range(0,len(nums)):
#             k -= 1 - nums[right]
#             # if k == 0:
#             #     result = max(result,right-left+1)
#             if k<0:
#                 k += 1-nums[left]
#                 left = left +1
            
#         return right - left + 1
class Solution:
    def longestOnes(self, nums, k):
        left = 0
        right = 0
        count = k
        result = 0
        while right < len(nums):
            if nums[right] == 0:
                count -= 1
            if count < 0:
                if nums[left] == 0:
                    count += 1
                left += 1
            right += 1
            result = max(result, right - left)
        return result
                
            
        




# class Solution:
#     def longestOnes(self, nums: List[int], k: int) -> int:
#         left = 0
#         for right in range(len(nums)):
#             # If we included a zero in the window we reduce the value of k.
#             # Since k is the maximum zeros allowed in a window.
#             k -= 1 - nums[right]
#             # A negative k denotes we have consumed all allowed flips and window has
#             # more than allowed zeros, thus increment left pointer by 1 to keep the window size same.
#             if k < 0:
#                 # If the left element to be thrown out is zero we increase k.
#                 k += 1 - nums[left]
#                 left += 1
#         return right - left + 1