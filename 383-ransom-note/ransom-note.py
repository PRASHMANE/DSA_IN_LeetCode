class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = Counter(magazine)

        for ch in ransomNote:
            if count.get(ch,0) == 0:
                return False
            else:
                count[ch]-=1
        return True