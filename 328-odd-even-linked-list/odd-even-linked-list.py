# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        evendummy=ListNode(0)
        odddummy=ListNode(0)

        even=evendummy
        odd=odddummy

        fast=slow=head

        while fast and fast.next:
            odd.next = ListNode(fast.val)
            even.next = ListNode(fast.next.val)
            fast=fast.next.next
            odd=odd.next
            even=even.next

        if fast :
            odd.next = ListNode(fast.val)
            odd=odd.next

        odd.next = evendummy.next

        return odddummy.next

            
        