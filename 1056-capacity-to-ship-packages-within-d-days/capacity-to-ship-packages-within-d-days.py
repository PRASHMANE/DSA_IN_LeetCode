class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def cap(arr,mid):
            day=1
            load=0
            for i in range(len(arr)):
                if load+arr[i] > mid:
                    day+=1
                    load=arr[i]

                else:
                    load+=arr[i]

            return day
        
        low=max(weights)
        high=sum(weights)

        while low <= high:
            mid = (low+high)//2

            day = cap(weights,mid)

            if day <= days:
                high=mid-1
            else:
                low=mid+1
        return low


