from typing import List
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        exp=sorted(heights)
        count=0
        for e,h in zip(exp,heights):
            if e != h:
                count+=1
        return count