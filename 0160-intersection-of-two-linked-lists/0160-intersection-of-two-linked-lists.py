# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pa=headA
        pb=headB
        curr1=headA
        n=0
        while(curr1):
            n+=1
            curr1=curr1.next
        m=0
        curr2=headB
        while(curr2):
            m+=1
            curr2=curr2.next
        d=abs(n-m)
        if(n>m):
            while(d>0 and pa):
                pa=pa.next
                d-=1
        else:
            while(d>0 and pb):
                pb=pb.next
                d-=1


        while(pa and pb):
            if(pa==pb):
                return pa
            pa=pa.next
            pb=pb.next

        return None
        

            