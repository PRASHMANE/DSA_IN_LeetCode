# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        ans=[]
        temp=head
        count=0

        while temp:
            if temp.val == 0 and count > 0:
                ans.append(count)
                count = 0
            elif temp.val != 0:
                count+=temp.val
            temp = temp.next
        
        dummy = ListNode(0)
        curr = dummy

        for i in ans:
            curr.next=ListNode(i)
            curr=curr.next
        return dummy.next
                