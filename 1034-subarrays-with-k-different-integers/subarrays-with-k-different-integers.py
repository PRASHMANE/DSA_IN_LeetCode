class Solution:
    def subarraysWithKDistinct(self, arr: List[int], k: int) -> int:
        def k_diff(nums,k):
            if k == 0:
                return 0
            hsh={}

            left=0
            n=len(nums)
            count=0

            for right in range(n):
                hsh[nums[right]]=hsh.get(nums[right],0)+1

                while len(hsh) > k:
                    hsh[nums[left]]-=1
                    if hsh[nums[left]] == 0:
                        del hsh[nums[left]]
                    left+=1
                    

                if len(hsh) <= k :
                    count+=right-left+1
            return count

        return k_diff(arr,k) - k_diff(arr,k-1)
            