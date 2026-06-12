class Solution:
    def makeGood(self, s: str) -> str:
        
        stack=[]
        if s=="":
            return s
        stack.append(s[0])
        for i in range(1,len(s)):
            if len(stack)!=0 and abs(ord(s[i])-ord(stack[-1]))==32:
                stack.pop()
            
            else:
                stack.append(s[i])
        return "".join(stack)
