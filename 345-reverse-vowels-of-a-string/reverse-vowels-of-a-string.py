class Solution:
    def reverseVowels(self, s: str) -> str:
        stack = []
        ans=""
        for i in s:
            if i == "a" or i == "A" or i == "e" or i == "E" or i == "i" or i == "I" or i == "o" or i=="O" or i == "u" or i == "U":
                stack.append(i)
        
        for i in s:
            if i == "a" or i == "A" or i == "e" or i == "E" or i == "i" or i == "I" or i == "o" or i=="O" or i == "u" or i == "U":
                ans+=stack.pop()
            else:
                ans+=i
        return ans

        