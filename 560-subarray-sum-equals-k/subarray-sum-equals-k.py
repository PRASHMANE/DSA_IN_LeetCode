class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        prefix=0
        hsh={0:1}
        count=0

        for i in nums:
            prefix+=i

            if prefix - k in hsh:
                count+=hsh[prefix-k]

            hsh[prefix]=hsh.get(prefix,0)+1
        
        return count
