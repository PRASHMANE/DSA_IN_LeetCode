class Solution:
    def rob(self, nums: List[int]) -> int:
        m = len(nums)
        if m <= 1:
            return nums[0]

        def solver(arr):
            n = len(arr)
            dp = [-1] * n
            
            def helper(i):
                if i>=n:
                    return 0
                
                if dp[i] != -1:
                    return dp[i]
                
                take = arr[i]+helper(i+2)
                nontake = helper(i+1)

                dp[i] = max(take,nontake)
                return dp[i]
            
            return helper(0)
        
        case1 = solver(nums[:-1])
        case2 = solver(nums[1:])

        return max(case1,case2)
        

            


        