class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        ind = -1
        m=len(needle)

        for i in range(len(haystack)):

            if haystack[i] == needle[0]:

                if haystack[i:i+m] == needle:
                    return i
        return ind


        