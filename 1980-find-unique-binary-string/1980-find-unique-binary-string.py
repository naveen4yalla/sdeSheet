# class Solution:
#     def findDifferentBinaryString(self, nums):
#         n = len(nums[0])
#         binary_strings = set(nums)

#         for i in range(2 ** n):
#             binary_string = bin(i)[2:].zfill(n)
#             if binary_string not in binary_strings:
#                 return binary_string
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        strSet = { s for s in nums }
        
        def backtrack(i, cur):
            if i == len(nums):
                res = "".join(cur)
                return None if res in strSet else res
            
            res = backtrack(i+1, cur)
            if res: return res
            
            cur[i] = "1"
            res = backtrack(i+1, cur)
            if res: return res
            
        return backtrack(0, ["0" for s in nums])