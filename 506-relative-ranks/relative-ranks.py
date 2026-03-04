class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        arr=sorted(score,reverse=True)

        hsh={}
        rank = 1
        for i in range(len(arr)):
            hsh[arr[i]] = i+1
        

        ans=[]

        for i in score:
            if hsh[i] == 1 :
                ans.append("Gold Medal")
            elif hsh[i] == 2:
                ans.append("Silver Medal")
            elif hsh[i] == 3:
                ans.append("Bronze Medal")
            else:
                ans.append(str(hsh[i]))

        return ans