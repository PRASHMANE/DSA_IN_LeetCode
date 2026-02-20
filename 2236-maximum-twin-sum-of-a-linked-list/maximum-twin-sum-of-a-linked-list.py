# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # 1) Find middle (slow-fast pointers)
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2) Reverse second half
        prev = None
        curr = slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # prev now points to start of reversed half

        # 3) Compute twin sums
        ans = 0
        first = head
        second = prev
        while second:
            ans = max(ans, first.val + second.val)
            first = first.next
            second = second.next

        return ans