class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        freq = Counter(nums)
        need = Counter()

        for num in nums:
            if freq[num] == 0:
                continue

            # Case 1: extend an existing subsequence
            if need[num] > 0:
                need[num] -= 1
                need[num + 1] += 1
                freq[num] -= 1

            # Case 2: start a new subsequence of length 3
            elif freq[num + 1] > 0 and freq[num + 2] > 0:
                freq[num] -= 1
                freq[num + 1] -= 1
                freq[num + 2] -= 1
                need[num + 3] += 1

            # Case 3: not possible
            else:
                return False

        return True
        
        