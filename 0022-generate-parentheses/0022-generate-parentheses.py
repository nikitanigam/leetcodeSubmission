class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        s=""
        close=n
        open=n
        def func(s,close,open):
            if len(s)==2*n:
                ans.append(s)
                return 

            if open > close:
                return  
            if open>0:
                func(s+"(",close,open-1)
            if close>0:
                func(s+")",close-1,open)

        func(s,close,open)
        return ans