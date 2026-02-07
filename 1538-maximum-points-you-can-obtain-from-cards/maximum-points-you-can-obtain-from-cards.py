class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        n=len(cardPoints)
        left=n-1
        right = k-1
        maxsum=sum(cardPoints[:k])
        count=maxsum

        for _ in range(k):
            count-=cardPoints[right]
            right-=1
            count+=cardPoints[left]
            left-=1
            maxsum=max(maxsum,count)
        return maxsum
        


