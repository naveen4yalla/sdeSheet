# class Solution:
#     def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
#         max_subset_size = 0

#         def backtrack(index, zeros, ones, subset_size):
#             nonlocal max_subset_size

#             if zeros > m or ones > n:
#                 return

#             if index == len(strs):
#                 max_subset_size = max(max_subset_size, subset_size)
#                 return

#             # Include the current string in the subset
#             zeros_included = strs[index].count('0')
#             ones_included = strs[index].count('1')
#             backtrack(index + 1, zeros + zeros_included, ones + ones_included, subset_size + 1)

#             # Exclude the current string from the subset
#             backtrack(index + 1, zeros, ones, subset_size)

#         backtrack(0, 0, 0, 0)

#         return max_subset_size
        
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        memo = {}

        def backtrack(i: int, zeros: int, ones: int) -> int:
            if i == len(strs) or (zeros == 0 and ones == 0):
                return 0

            if (i, zeros, ones) in memo:
                return memo[(i, zeros, ones)]

            zeros_count = strs[i].count('0')
            ones_count = strs[i].count('1')

            if zeros >= zeros_count and ones >= ones_count:
                include = backtrack(i + 1, zeros - zeros_count, ones - ones_count) + 1
                exclude = backtrack(i + 1, zeros, ones)
                memo[(i, zeros, ones)] = max(include, exclude)
            else:
                memo[(i, zeros, ones)] = backtrack(i + 1, zeros, ones)

            return memo[(i, zeros, ones)]

        return backtrack(0, m, n)
