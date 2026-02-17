class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        max_radius = 0
        
        for house in houses:
            # Find insertion position
            idx = bisect.bisect_left(heaters, house)
            
            # Distance to left heater
            left_dist = float('inf') if idx == 0 else house - heaters[idx - 1]
            
            # Distance to right heater
            right_dist = float('inf') if idx == len(heaters) else heaters[idx] - house
            
            # Closest heater distance
            min_dist = min(left_dist, right_dist)
            
            max_radius = max(max_radius, min_dist)
        
        return max_radius
