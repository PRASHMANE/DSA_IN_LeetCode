class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        arr=[[0 for _ in range(n)]for _ in range(n)]
        val=1
        top,bottom,left,right=0,n-1,0,n-1
        while left <= right and top <= bottom:
            for i in range(left,right+1):
                arr[top][i]=val
                val+=1
            top+=1

            for i in range(top,bottom+1):
                arr[i][right]=val
                val+=1
            right-=1

            if top <= bottom:
                for i in range(right,left-1,-1):
                    arr[bottom][i]=val
                    val+=1
                bottom-=1

            if left <= right:
                for i in range(bottom,top-1,-1):
                    arr[i][left]=val
                    val+=1
                left+=1
            
        return arr
                
