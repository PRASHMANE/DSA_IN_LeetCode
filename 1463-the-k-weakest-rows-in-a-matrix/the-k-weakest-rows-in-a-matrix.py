class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:

        m=len(mat)
        n=len(mat[0])

        hst={}

        for i in range(m):
            count=0
            for j in range(n):
                if mat[i][j]==0:
                    count+=1
            hst[i]=count
        
        hst = dict(sorted(hst.items(),key = lambda x : x[1],reverse=True))
        ans=[]
        ct=0
        for i in hst:
            if ct < k:
                ans.append(i)
                ct+=1
        return ans

                
        