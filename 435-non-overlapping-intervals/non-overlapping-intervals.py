class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : x[1])

        pre_val = intervals[0][1]

        count=0

        for interval in intervals[1:]:
            if interval[0] < pre_val:
                count+=1
            else:
                pre_val = interval[1]
        return count