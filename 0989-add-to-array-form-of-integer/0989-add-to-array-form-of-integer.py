class Solution:
    def addToArrayForm(self, nums: List[int], k: int) -> List[int]:
        nums.reverse()
        i = 0
        while k:
            digit = k%10
            if i < len(nums):
                nums[i]+=digit
            else:
                nums.append(digit)
            
            carry = nums[i]//10
            nums[i] = nums[i] % 10
            
            k= k//10
            k+=carry
            i+=1
        nums.reverse()
        return nums
        