class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x
        dig = 0
        

        while temp > 0:
            rem = temp % 10
            dig = (dig * 10) + rem
            temp = temp//10
        if dig == x:
            return True
        return False
        