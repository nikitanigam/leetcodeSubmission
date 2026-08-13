class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        t=0
        n=len(tickets)
        i=0
        while(tickets [k]):
            if tickets[i]>0:
                tickets[i]-=1
                t+=1
            i=(i+1)%n

        return t
            
            


        