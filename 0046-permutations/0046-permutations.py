class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        p=[]
        used=[False]*len(nums)
        def backtrack(p):
            if len(p)==len(nums):
                ans.append(p.copy())
                return
             
            for i in range(len(nums)):
                if used[i]:
                    continue
                p.append(nums[i])
                used[i]=True
                backtrack(p)
                p.pop()
                used[i]=False

        backtrack(p)

        return ans
