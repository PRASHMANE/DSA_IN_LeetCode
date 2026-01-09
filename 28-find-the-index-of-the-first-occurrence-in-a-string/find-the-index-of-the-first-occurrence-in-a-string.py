class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

    
        m=len(needle)
        ind = -1

        for i in range(len(haystack)):

            if haystack[i] == needle[0]:

                if haystack[i:i+m] == needle:
                    return i
        return ind
                


        