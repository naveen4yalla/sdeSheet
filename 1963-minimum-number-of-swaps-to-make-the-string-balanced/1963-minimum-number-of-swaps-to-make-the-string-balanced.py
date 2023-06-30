class Solution:
    def minSwaps(self, s: str) -> int:
        fixes_applied = 0
        current_open = 0

        for c in s:
            if c == '[':            # Open is always considered OK
                current_open += 1

            elif current_open > 0:  # Valid Closings are OK
                current_open -= 1
                
            else:                   # Invalid Closings Require a Fix
                fixes_applied += 1
                current_open += 1

        return fixes_applied