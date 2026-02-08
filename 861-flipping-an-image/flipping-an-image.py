class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        ans=[]

        for i in image:
            ans.append(i[::-1])
        #return [list(row) for row in zip(*ans)][::-1]
        m=len(image)
        n=len(image[0])
        for i in range(m):
            for j in range(n):
                if ans[i][j] == 1:
                    ans[i][j]=0
                else:
                    ans[i][j]=1
        return ans
        