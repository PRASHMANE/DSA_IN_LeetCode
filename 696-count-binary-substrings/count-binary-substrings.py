class Solution:
    def countBinarySubstrings(self, s: str) -> int:

        res = 0
        prev_count = 0
        curr_count = 1
        
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                curr_count += 1
            else:
                res += min(prev_count, curr_count)
                prev_count = curr_count
                curr_count = 1
        
        res += min(prev_count, curr_count)
        return res

        