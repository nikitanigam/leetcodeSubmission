# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        dummy=ListNode()
        dummy.next=head
        prev=dummy
        while(prev.next and prev.next.next):
            first=prev.next
            second=first.next
            nextpair=second.next
            first.next=nextpair
            second.next=first
            prev.next=second      
            prev=first
        return dummy.next     
