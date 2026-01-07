class Solution:
    def totalMoney(self, n: int) -> int:
        fullWeeks = n // 7
        rem = n % 7
        
        # total from full weeks
        total_full = fullWeeks * 28 + 7 * (fullWeeks * (fullWeeks - 1) // 2)
        
        # total from remaining days
        weekStart = fullWeeks + 1
        total_rem = rem * weekStart + (rem * (rem - 1) // 2)
        
        return total_full + total_rem
