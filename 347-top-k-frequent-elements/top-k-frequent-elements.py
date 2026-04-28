class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = Counter(nums)
        count = dict(sorted(count.items() , key = lambda x:x[1] , reverse=True))

        return [key for key in count][:k]