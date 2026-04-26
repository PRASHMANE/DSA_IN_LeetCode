class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        
        left = 0
        right = len(tokens)-1

        score = 0

        tokens.sort()
    

        while left <= right:
            if tokens[left] <= power:
                power-=tokens[left]
                score+=1
                left+=1
            else:
                if score > 0 and left!= right:
                    score-=1
                    power+=tokens.pop()
                    right-=1
                else:
                    break
        return score
            
