class Solution:
    def concatenatedBinary(self, n: int) -> int:
        shifter = 1
        val = 1
        answer = 0
        mod = 10**9 + 7
        
        for a in range(1, n + 1):
            if val * 2 == a:
                shifter += 1
                val = a
            answer = ((answer << shifter) | a) % mod
            
        return answer