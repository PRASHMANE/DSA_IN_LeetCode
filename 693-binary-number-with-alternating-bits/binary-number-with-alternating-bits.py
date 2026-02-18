class Solution:
    def hasAlternatingBits(self, n: int) -> bool:

        bit=bin(n)[2:]

        for i in range(1,len(bit)):
            if bit[i] == bit[i-1]:
                return False
        return True
        