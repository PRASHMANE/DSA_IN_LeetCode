class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        hsh={0:1}
        count=0
        sum=0

        for num in nums:
            sum+=num
            if sum-k in hsh:
                count += hsh[sum-k]
            hsh[sum]=hsh.get(sum,0)+1
        return count
