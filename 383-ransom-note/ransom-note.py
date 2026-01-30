class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter={}

        for ch in magazine:
            if ch in counter:
                counter[ch]=counter.get(ch,0)+1
            else:
                counter[ch]=1
        
        for ch in ransomNote:
            if ch not in counter or counter[ch] == 0:
                return False
            counter[ch]-=1
        return True
        