class Solution:
    def isAnagram(self,s1, s2):
    # Convert strings to lowercase to ignore case sensitivity
        s1 = s1.lower()
        s2 = s2.lower()

        # If the lengths of the strings are not equal, they cannot be anagrams
        if len(s1) != len(s2):
            return False

        # Create dictionaries to store character frequencies
        freq1 = {}
        freq2 = {}

        # Count frequencies of characters in the first string
        for char in s1:
            freq1[char] = freq1.get(char, 0) + 1

        # Count frequencies of characters in the second string
        for char in s2:
            freq2[char] = freq2.get(char, 0) + 1

        # Compare the character frequencies
        return freq1 == freq2
            
        