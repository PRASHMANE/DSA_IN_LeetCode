class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        count=0
        left=0
        sum1=0
        n= len(arr)

        for right in range(n):

            sum1 += arr[right]

            while right - left + 1 > k:
                sum1-=arr[left]
                left+=1
            
            if right - left + 1 == k and sum1 // k >= threshold:
                count+=1
        
        return count