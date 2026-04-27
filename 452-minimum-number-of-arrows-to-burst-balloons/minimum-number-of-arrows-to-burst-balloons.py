class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x:x[1])
        arrow = 1
        ends = points[0][1]

        for start,end in points:
            if start > ends:
                arrow+=1
                ends = end
        return arrow