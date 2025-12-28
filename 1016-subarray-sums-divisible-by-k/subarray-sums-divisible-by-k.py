from collections import defaultdict

class Solution:

    def subarraysDivByK(self,nums, k):
        mp = defaultdict(int)
        mp[0] = 1

        prefix_sum = 0
        count = 0

        for num in nums:
            prefix_sum += num
            mod = (prefix_sum % k + k) % k

            count += mp[mod]
            mp[mod] += 1

        return count
