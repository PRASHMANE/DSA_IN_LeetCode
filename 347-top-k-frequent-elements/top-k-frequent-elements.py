class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        count = dict(sorted(count.items(),key=lambda x:x[1],reverse=True))
        ans=[]
        for i in count:
            if k > 0:
                ans.append(i)
                k-=1
        return ans
        