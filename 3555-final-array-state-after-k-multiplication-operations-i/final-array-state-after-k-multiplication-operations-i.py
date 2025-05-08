class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        def find_min(arr):
            min=arr[0]
            ind=0
            for i in range(len(arr)):
                if min > arr[i]:
                    min = arr[i]
                    ind=i
            arr[ind]= arr[ind]*multiplier
            

        for i in range(k):
            find_min(nums)
        
        return nums
            
        