class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        n=len(pushed)
        stack=[]
        j=0
        for i in range(n):
            stack.append(pushed[i])
            while(stack and stack[-1]==popped[j] and j<n):
                stack.pop()
                j+=1
        
        if stack==[]:
            return True
        else:
            return False

        