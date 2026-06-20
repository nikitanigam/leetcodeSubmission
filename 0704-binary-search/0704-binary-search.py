class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        flag=False
        while(l<=r):
            mid=int((l+r)/2)
            if(target==nums[mid]):
                flag=True
                break
            elif(target>nums[mid]):
                l=mid+1
            else:
                r=mid-1
        if(flag==True):
            return mid
        else:
            return -1
