from collections import Counter
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        temp=words[:]
        ans=[]
        for ch in temp[0]:
            found=True
            for i in range(1,len(words)):
                if ch in temp[i]:
                    temp[i]=temp[i].replace(ch,"",1)
                else:
                    found = False
                    break
            if found:
                ans.append(ch)
        return ans
                