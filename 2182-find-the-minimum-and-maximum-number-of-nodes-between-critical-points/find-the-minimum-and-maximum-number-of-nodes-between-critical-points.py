# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:

        arr = []

        temp = head

        while temp:
            arr.append(temp.val)
            temp = temp.next
       

        n = len(arr)
        if n <= 2:
            return [-1,-1]
        
        critical = [] 
        for i in range(1,n-1):
            if (arr[i-1] > arr[i] and arr[i+1] > arr[i]) or (arr[i-1] < arr[i] and arr[i+1] < arr[i]):
                critical.append(i+1)
        
        maxi = float("-inf")
        mini = float("inf")
        m = len(critical)
        if m < 2:
            return [-1,-1]

        elif m == 2:
            return [critical[1]-critical[0],critical[1]-critical[0]]
        mini = float("inf")
        for i in range(1,m):
            mini = min(mini,critical[i] - critical[i-1])
        maxi = critical[-1]-critical[0]
        return [mini,maxi]