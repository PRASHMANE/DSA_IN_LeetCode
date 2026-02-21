class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        # Step 1: transform array
        arr = []
        for num in nums:
            if num == target:
                arr.append(1)
            else:
                arr.append(-1)
        
        count = 0
        
        # Step 2: check all subarrays
        for i in range(n):
            total = 0
            for j in range(i, n):
                total += arr[j]
                if total > 0:
                    count += 1
        
        return count