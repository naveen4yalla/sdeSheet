class Solution:
    def nextGreaterElement(self,nums1, nums2):
        stack= [ ]
        ds = {}
        for f in range(len(nums2)):
            while stack and nums2[f] > stack[-1]:
                ds[stack.pop()] = nums2[f]
            stack.append(nums2[f])
        while stack:
            ds[stack.pop()] = -1
        result = [-1] * len(nums1)
        for f in range(len(nums1)):
            result[f]  = ds[nums1[f]]
        return result
                
        