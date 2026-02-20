class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        
        weekday = datetime.date(year, month, day).weekday()

        
        mapping = [
            "Monday","Tuesday","Wednesday",
            "Thursday","Friday","Saturday","Sunday"
        ]
        return mapping[weekday]