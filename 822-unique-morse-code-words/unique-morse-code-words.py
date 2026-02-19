class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        
        sym=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        ans=set()

        for word in words:
            st=""
            for ch in word:
                st+=sym[ord(ch)- ord('a')]
            ans.add(st)
        
        return len(ans)

