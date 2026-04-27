class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        ans=[]
        ans.append(intervals[0])

        for start,end in intervals:
            if ans[-1][1] >= start :
                if end > ans[-1][1]:
                    ans[-1][1] = end
            else:
                ans.append([start,end])
        return ans

