class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        ans=letters[0]
        n=len(letters)
        lst=[]
        for i in letters:
            if i not in lst:
                lst.append(i)
        for i in range(len(lst)):
            if lst[i] == target and i == len(lst)-1:
                return lst[0]
            elif lst[i] == target:
                return lst[i+1]

        for i in letters:
            if ord(i) > ord(target):
                return i
        return ans