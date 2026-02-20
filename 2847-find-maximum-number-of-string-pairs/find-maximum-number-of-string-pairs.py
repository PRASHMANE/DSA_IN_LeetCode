class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        
        count=0
        n=len(words)

        for i in range(n):
            for j in range(i,n):
                if i != j:
                    if words[i] == words[j][::-1]:
                        count+=1
        
        return count
