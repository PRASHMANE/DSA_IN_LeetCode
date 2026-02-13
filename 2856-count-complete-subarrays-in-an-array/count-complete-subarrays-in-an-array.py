class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        
        k = len(set(nums))

        def k_less(arr,k):

            hsh={}
            count=0
            left=0
            n=len(arr)

            for right in range(n):
                hsh[arr[right]]=hsh.get(arr[right],0)+1

                while len(hsh) > k:
                    hsh[arr[left]]-=1
                    if hsh[arr[left]]==0:
                        del hsh[arr[left]]
                    left+=1
                
                if len(hsh) <= k:
                    count+= right-left+1
            
            return count

        return k_less(nums,k)-k_less(nums,k-1)