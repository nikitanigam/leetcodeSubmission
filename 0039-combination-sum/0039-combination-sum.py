class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        p=[]
        def func(p,start):
            if sum(p)==target and p not in ans:
                ans.append(p.copy())
                return
            if sum(p)>target:
                return
            for i in range(start,len(candidates)):
                p.append(candidates[i])
                func(p,i)
                p.pop()
        func(p,0)
        return ans
        