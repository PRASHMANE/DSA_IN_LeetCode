class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        m1, m2 = float('inf'), float('inf')
        for x in nums[1:]:
            if x < m1:
                m2 = m1
                m1 = x
            elif x < m2:
                m2 = x
        return nums[0] + m1 + m2


        