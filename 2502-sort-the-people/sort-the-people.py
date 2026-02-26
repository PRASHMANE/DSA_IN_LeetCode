class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        hsh={}

        for i , j in zip(names,heights):
            hsh[j] = i
        
        hsh=dict(sorted(hsh.items(),key = lambda x: x[0],reverse = True))

        ans=[]
        for i in hsh.values():
            ans.append(i)
        return ans