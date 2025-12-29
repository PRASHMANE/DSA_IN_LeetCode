class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand) % groupSize != 0:
            return False
        while hand:
            hand.sort()
            s=hand[0]
            for x in range(s,s+groupSize):
                if x not in hand:
                    return False
                hand.remove(x)
            
        return True