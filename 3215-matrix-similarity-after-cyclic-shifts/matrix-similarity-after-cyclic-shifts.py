class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:

        def reverse(nums,start,end):
            while start < end:
                temp = nums[start]
                nums[start] = nums[end]
                nums[end] = temp
                start+=1
                end-=1
        
        n = len(mat)
        m = len(mat[0])
        k = k % m

        arr=[[0]*m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                arr[i][j] = mat[i][j]
        

        for i in range(n):
            if i % 2 == 0:
                d = m - k
                reverse(arr[i],0,d-1)
                reverse(arr[i],d,m-1)
                reverse(arr[i],0,m-1)
            else:
                reverse(arr[i],0,k-1)
                reverse(arr[i],k,m-1)
                reverse(arr[i],0,m-1)

        for i in range(n):
            for j in range(m):
                if arr[i][j] != mat[i][j]:
                    return False
        
        return True

        