class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        
        hex_map = "0123456789abcdef"
        result = ""
        
        # handle negative numbers using 32-bit mask
        num &= 0xFFFFFFFF
        
        while num > 0:
            result = hex_map[num & 15] + result
            num >>= 4
        
        return result