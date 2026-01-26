class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:

        filte = s.replace("-","").upper()
        result=[]
        count=0

        for i in filte[::-1]:
            if count == k:
                result.append("-")
                count = 0
            count+=1
            result.append(i)

        return "".join(result[::-1])
        