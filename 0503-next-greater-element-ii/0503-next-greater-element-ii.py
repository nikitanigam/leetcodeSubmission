class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack=[]
        for i in range(len(nums)-1,-1,-1):
            stack.append(nums[i])
        
        r=[-1]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            while(len(stack)!=0)and(nums[i]>=stack[-1]):
                stack.pop()
            if(len(stack)==0):
                r[i]=-1
            else:
                r[i]=stack[-1]
            stack.append(nums[i])
        return r