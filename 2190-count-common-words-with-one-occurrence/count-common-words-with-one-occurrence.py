class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        temp1=Counter(words1)
        temp2=Counter(words2)
        count=0

        for ch in temp1:
            if temp1[ch] == 1 and temp2.get(ch,0) == 1:
                count+=1
        return count