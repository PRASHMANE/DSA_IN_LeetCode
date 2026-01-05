class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        freq = [0] * 101
        
        # Count frequency
        for num in nums:
            freq[num] += 1
        
        # Prefix sum
        for i in range(1, 101):
            freq[i] += freq[i - 1]
        
        # Build answer
        ans = []
        for num in nums:
            if num == 0:
                ans.append(0)
            else:
                ans.append(freq[num - 1])
        return ans
        