class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.findall(r"[a-zA-Z]+", paragraph.lower())
        
        banned_set = set(banned)
        freq = collections.Counter()
        
        for w in words:
            if w not in banned_set:
                freq[w] += 1
        
        # Return the word with maximum count
        return freq.most_common(1)[0][0]