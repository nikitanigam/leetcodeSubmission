class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l=0
        r=len(matrix)-1
        res=[]
        while(l<=r):
            mid=int((l+r)/2)
            if (matrix[mid][0]<=target and target<=matrix[mid][-1]):
                res=matrix[mid]
                break
            elif(target<matrix[mid][0]):
                r=mid-1
            else:
                l=mid+1

        i=0
        j=len(res)-1
        while(i<=j):
            m=int((i+j)/2)
            if (target==res[m]):
                return True
            elif(target<res[m]):
                j=m-1
            else:
                i=m+1
        return False
        