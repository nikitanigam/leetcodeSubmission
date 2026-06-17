class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack=[]
        nums1=[]
        for i in num:
            nums1.append(int(i))
        for i in range(len(num)):
            while(stack and stack[-1]>nums1[i] and k>0):
                stack.pop()
                k-=1
            stack.append(nums1[i])
        if(len(stack)!=0):
            while(k>0):
                stack.pop()
                k-=1

        r=""
        for i in stack:
            r=r+str(i)
        r=r.lstrip("0")
        if r=="":
            r=r+"0"
        return r  