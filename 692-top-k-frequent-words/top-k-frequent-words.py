class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words1=sorted(words)
        w_count = Counter(words1)
        ans=[]
        w=dict(sorted(w_count.items(),key=lambda x:x[1], reverse=True))
        for i in w:
            if k > 0:
                ans.append(i)
                k-=1
        return ans
        