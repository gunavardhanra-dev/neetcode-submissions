# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        pointerA,pointerB=list1,list2
        dummy_head=ListNode(0)
        tail=dummy_head
        while pointerA and pointerB:
            if pointerA.val>=pointerB.val:
                tail.next=pointerB
                tail=tail.next
                pointerB=pointerB.next
            else:
                tail.next=pointerA
                tail=tail.next
                pointerA=pointerA.next
        tail.next=pointerA or pointerB
        return dummy_head.next

        