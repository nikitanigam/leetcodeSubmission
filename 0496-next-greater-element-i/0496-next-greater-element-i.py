class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        d={}
        for i in range(len(nums2)-1,-1,-1):
            while(len(stack)!=0)and(nums2[i]>=stack[-1]):
                stack.pop()
            if len(stack)==0:
                d[nums2[i]]=-1
            else:
                d[nums2[i]]=stack[-1]

            stack.append(nums2[i])
        answer=[]
        for i in nums1:
            answer.append(d[i])
        return answer
        