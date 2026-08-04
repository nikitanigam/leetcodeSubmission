class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        p=[]
        def backtrack(start):
            ans.append(p.copy())

            for i in range(start,len(nums)):
                p.append(nums[i])
                backtrack(i+1)
                p.pop()

        backtrack(0)
        return ans
        