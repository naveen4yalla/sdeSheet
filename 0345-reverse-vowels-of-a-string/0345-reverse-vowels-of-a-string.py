class Solution:
    def reverseVowels(self, s: str) -> str:
        left = 0
        right = len(s) - 1
        rs = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        s_list = list(s)  # Convert string to list
        
        while left < right:
            while (left < right) and s[left] not in rs:
                left += 1
            while (left < right) and s[right] not in rs:
                right -= 1
                
            if left < right:
                s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1
        
        reversed_s = ''.join(s_list)  # Convert list back to string
        return reversed_s


                
            
        