class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1 = set(nums1)
        s2 = set(nums2)
        r1=list(set(x for x in nums1 if x not in s2))
        r2=list(set(x for x in nums2 if x not in s1))
        return [r1,r2]
        