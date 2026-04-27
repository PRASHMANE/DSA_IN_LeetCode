class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : x[1])

        prev = intervals[0][1]

        count= 0

        for start , end in intervals[1:]:
            if prev > start :
                count+=1
            else:
                prev = end
        return count