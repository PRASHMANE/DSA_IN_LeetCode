class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        freq = Counter(deck).values()
        
        # Compute GCD of all frequencies
        g = 0
        for count in freq:
            g = math.gcd(g, count)
        
        # If gcd >= 2, we can partition
        return g >= 2