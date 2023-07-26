from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        totalShifts = 0
        result = []
        
        for i in range(len(shifts)-1, -1, -1):
            totalShifts = (totalShifts + shifts[i]) % 26
            index = (ord(s[i]) - ord('a') + totalShifts) % 26
            index = index + ord('a')
            result.append(chr(index))
            
        return ''.join(result[::-1])
