# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        pa=l1
        pb=l2
        curr=ListNode()
        dummy=curr
        s=0
        carry=0
        while(pa and pb):
            s=pa.val+pb.val+carry
            digit=s%10
            carry=s//10
            newnode=ListNode(digit)
            curr.next=newnode
            curr=newnode
            pa=pa.next
            pb=pb.next
     

        while(pa):
            s=pa.val+carry
            digit=s%10
            carry=s//10
            newnode=ListNode(digit)
            curr.next=newnode
            curr=newnode
            pa=pa.next
        while(pb):
            s=pb.val+carry
            digit=s%10
            carry=s//10
            newnode=ListNode(digit)
            curr.next=newnode
            curr=newnode
            pb=pb.next
        if (carry!=0):
            newnode=ListNode(carry)
            curr.next=newnode
        return dummy.next
        
        
