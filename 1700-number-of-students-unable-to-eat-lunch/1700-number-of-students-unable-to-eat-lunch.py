class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        m=0
        n=0
        for i in students:
            if i==0:
                m+=1
            else:
                n+=1
        
        for i in range(len(sandwiches)):
            if sandwiches[i]==0:
                if m==0:
                    break
                m-=1
            if sandwiches[i]==1:
                if n==0:
                    break
                n-=1

        return m+n

        