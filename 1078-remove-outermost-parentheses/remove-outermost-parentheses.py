class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        mp={
            ")":"(",
            "}":"{",
            "]":"["
        }

        stack=[]
        ans=""
        for i in s:
            if i in mp:
                if len(stack) > 1:
                    stack.pop()
                    ans+=i
                else:
                    stack.pop()
            else:
                stack.append(i)
                if len(stack) > 1:
                    ans+=i
                
        return ans

        