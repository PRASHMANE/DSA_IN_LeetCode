class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:

        uni=set()
        for i in word1:
            uni.add(i)
        for i in word2:
            uni.add(i)
        
        count1=Counter(word1)
        count2=Counter(word2)

        for i in uni:
            if abs(count1.get(i,0)-count2.get(i,0)) > 3:
                return False
        
        return True
        