class Solution:
    def strStr(self, haystack, needle):
        if haystack is None or needle is None:
            return -1
        if haystack == needle:
            return 0
        print((len(haystack)-len(needle)+1))
        count = len(needle)
        for f in range((len(haystack)-len(needle)+1)):
            print(haystack[f:f+count])
            if haystack[f:f+count] == needle:
                return f
        return -1
        