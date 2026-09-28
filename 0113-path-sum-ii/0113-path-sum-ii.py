# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left                        
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        ans=[]
        arr=[]
        def func(root,targetSum,arr):
            if root is None:
                return 
            targetSum-=root.val
            arr.append(root.val)
            if root.left==None and root.right==None:
                if targetSum==0:
    
                    ans.append(arr.copy())

                arr.pop()
                return 

            func(root.left,targetSum,arr)
            func(root.right,targetSum,arr)
            arr.pop()
            

        func(root,targetSum,arr)
        return ans 
                    


        