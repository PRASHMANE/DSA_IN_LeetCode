class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key  = lambda x : (x[0],-x[1]))

        count =0 
        last_count = 0
        for start , end in intervals:
            if end > last_count:
                count+=1
                last_count = end
        return count