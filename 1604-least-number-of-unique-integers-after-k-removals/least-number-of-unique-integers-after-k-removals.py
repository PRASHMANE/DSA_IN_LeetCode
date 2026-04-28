class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:

        count = dict(sorted(Counter(arr).items() , key = lambda x:x[1]))

        for key , val in count.items():
            while k > 0:
                if val == 0:
                    break
                elif val >= k:
                    val-=k
                    k=0
                    count[key] = val
                elif val < k:
                    k -= val
                    val=0
                    count[key] = val
                    

        ans = 0

        for key , val in count.items():
            if val > 0:
                ans+=1
        
        
        return ans