class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:

        ans=[]
        arr.sort()
        minum=float("inf")
        for i in range(1,len(arr)):
            if arr[i] - arr[i-1] <= minum:
                minum=min(minum,arr[i]-arr[i-1])

        for i in range(1,len(arr)):
            if arr[i]-arr[i-1] == minum:
                ans.append([arr[i-1],arr[i]])
        return ans
        