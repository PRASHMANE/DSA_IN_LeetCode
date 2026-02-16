class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ans=[]
        for i in range(len(words)):
            for word in words[i]:
                if word == x:
                    ans.append(i)
                    break
        return ans