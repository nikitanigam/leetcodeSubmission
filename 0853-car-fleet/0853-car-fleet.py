class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time=[]
        for p,s in zip(position,speed):
            t=(target-p)/s
            time.append([p,t])
        f=0
        ft=0
        time.sort()
        for i in range(len(time)-1,-1,-1):
            cur=time[i][1]
            if(cur>ft):
                f+=1
                ft=cur
        return f

        