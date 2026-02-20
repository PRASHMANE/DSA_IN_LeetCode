class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        count=0
        
    

        for word in words:
            freq=Counter(chars)
            found=True
            for ch in word:
                if freq.get(ch,0) == 0:
                    found=False
                    break
                else:
                    freq[ch]-=1
            
            if found:
                count+=len(word)
        
        return count