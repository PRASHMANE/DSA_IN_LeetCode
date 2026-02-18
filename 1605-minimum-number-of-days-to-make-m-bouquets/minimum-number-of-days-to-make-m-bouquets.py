class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        def count_bouq(arr,m,k,mid):

            cnt=0
            count_b=0
            for i in range(len(arr)):
                if arr[i ] <= mid:
                    cnt+=1
                else:
                    if cnt >= k:
                        count_b += cnt//k
                    cnt=0
            count_b += cnt//k
            if count_b >= m:
                return True

            return False
        

        n = len(bloomDay)

        if n < m*k:
            return -1
        
        low = min(bloomDay)
        high=max(bloomDay)

        ans = high

        while low <= high:
            mid = (low+high)//2

            if count_bouq(bloomDay,m,k,mid):
                ans = min(ans,mid)
                high = mid-1
            else:
                low = mid+1
        
        return ans
                    
        