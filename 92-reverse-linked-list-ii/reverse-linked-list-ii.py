# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        stack=[]
        idx=1
        dummy=ListNode(0)
        curr = dummy
        temp=head

        while temp:
            if idx >= left and idx <= right:
                stack.append(temp.val)
            idx+=1
            temp=temp.next
        
        temp = head
        idx=1
        while temp:
            if idx >= left and idx <= right:
                curr.next = ListNode(stack.pop())
                curr=curr.next
                temp = temp.next
                idx+=1
            else:
                curr.next = ListNode(temp.val)
                curr=curr.next
                temp = temp.next
                idx+=1
        return dummy.next



        