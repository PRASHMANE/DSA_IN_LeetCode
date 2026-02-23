class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        # Step 1: create order map
        rank = {ch: i for i, ch in enumerate(order)}
        
        # Step 2: compare adjacent words
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]
            
            # Compare characters
            for j in range(min(len(w1), len(w2))):
                
                if w1[j] != w2[j]:
                    if rank[w1[j]] > rank[w2[j]]:
                        return False
                    break
            else:
                # Prefix case
                if len(w1) > len(w2):
                    return False
        
        return True