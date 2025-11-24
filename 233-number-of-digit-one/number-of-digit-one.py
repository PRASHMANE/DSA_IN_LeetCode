class Solution:
    def countDigitOne(self, n: int) -> int:
        if n == 0:
            return 0

        count = 0
        position = 1  # 1 → units, 10 → tens, 100 → hundreds
    
        while position <= n:
            high = n // (position * 10)
            curr = (n // position) % 10
            low = n % position
            
            if curr == 0:
                count += high * position
            elif curr == 1:
                count += high * position + (low + 1)
            else:
                count += (high + 1) * position
            
            position *= 10
        
        return count