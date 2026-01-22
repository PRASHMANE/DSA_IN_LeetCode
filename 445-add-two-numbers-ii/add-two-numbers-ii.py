# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def val(temp):
            s=""
            while temp:
                s+= str(temp.val)
                temp=temp.next
            return int(s)

        temp1=l1
        temp2=l2

        val1=val(temp1)
        val2=val(temp2)

        temp1=l1
        temp2=l2

        ans = val1+val2

        dummy=ListNode(0)
        curr=dummy

        for i in str(ans):
            curr.next=ListNode(int(i))
            curr=curr.next
        
        return dummy.next
