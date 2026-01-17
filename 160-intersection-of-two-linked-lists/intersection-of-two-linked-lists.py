# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        def find_len(temp):
            length=0
            while temp:
                length+=1
                temp=temp.next
            return length


        def move(temp,val):
            for i in range(val):
                temp=temp.next
            return temp

        temp1 = headA
        temp2 = headB

        len1=find_len(temp1)
        len2=find_len(temp2)

        temp1 = headA
        temp2 = headB

        if len1 > len2:
            temp1=move(temp1,len1-len2)
        else:
            temp2 = move(temp2,len2-len1)

        while temp1:
            if temp1 == temp2:
                return temp1
            temp1 = temp1.next
            temp2 = temp2.next
        return None
            



