# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow=head
        fast=head
        while(fast and fast.next):
            slow=slow.next
            fast=fast.next.next
        curr=slow
        prev=None
        while(curr):
            nt=curr.next
            curr.next=prev
            prev=curr
            curr=nt
        p=head
        while(prev):
            if(p.val!=prev.val):
                return False
            p=p.next
            prev=prev.next
        return True        