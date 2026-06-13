class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        stack=[]
        answer=[0]*n
        for i in range(n-1,-1,-1):
            if(len(stack)==0):
                answer[i]=0
            else:

                while(len(stack)!=0)and (temperatures[i]>=temperatures[stack[-1]]):
                    stack.pop()
                if(len(stack)==0):
                    answer[i]=0
                else:
                    answer[i]=abs(i-stack[-1])
            stack.append(i)
        return answer
