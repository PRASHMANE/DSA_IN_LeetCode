class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        left=1
        right=min(ranks)*cars*cars

        def can_repair_car(time):
            total_car_replace=0
            for rank in ranks:
                cars_repairs=int((time/rank)**0.5)
                total_car_replace += cars_repairs
                if total_car_replace >= cars:
                    return True
            return False

        while left < right:
            mid = (left + right)//2
            if can_repair_car(mid):
                right = mid
            else:
                left = mid+1
        return left