class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1=s1.split(" ")
        s2=s2.split(" ")

        s1_count=Counter(s1)
        s2_count=Counter(s2)

        s1 = set(s1)
        s2=set(s2)

        ans=[]
        for i in list(s1-s2):
            if s1_count[i] == 1:
                ans.append(i)
        for i in list(s2-s1):
            if s2_count[i] == 1:
                ans.append(i)
        return ans
        