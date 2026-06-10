# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow,fast=head,head
        while fast and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
        prev=None
        current=slow
        while current:
            next_p=current.next
            current.next=prev
            prev=current
            current=next_p
        while prev:
            if head.val==prev.val:
                head=head.next
                prev=prev.next
            else: return False
        return True