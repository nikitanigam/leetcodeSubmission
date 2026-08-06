class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]
        p=[]
        def func(p,start):
            if len(p)==k:
                ans.append(p.copy())
                return
            if len(p)>k:
                return
            for i in range(start,n+1):
                p.append(i)
                func(p,i+1)
                p.pop()
        func(p,1)
        return ans
        