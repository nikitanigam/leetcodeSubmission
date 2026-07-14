# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        small=ListNode()
        sh=small
        greater=ListNode()
        gh=greater
        curr=head
        while(curr):
            if curr.val<x:
                small.next=curr
                small=small.next
            else:
                greater.next=curr
                greater=greater.next


            curr=curr.next

        greater.next=None
        small.next=gh.next
        return sh.next