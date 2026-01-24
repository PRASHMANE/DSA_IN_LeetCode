class Solution:
    def myAtoi(self, s: str) -> int:

        s = s.strip()
        if not s:
            return 0

        sign=1
        if s[0] == "+" or s[0] == "-":
            sign = -1 if s[0] == "-" else 1
            s=s[1:]
        num=""
        for i in s:
            if i.isdigit():
                num+=i
            else:
                break
        if not num:
            return 0

        res=sign*int(num)

        return max(-2**31,min(res,2**31 - 1))
        