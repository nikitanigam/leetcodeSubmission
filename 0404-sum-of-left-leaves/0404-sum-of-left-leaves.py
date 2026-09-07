# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        sum=0
        def func(root,isleft):
            nonlocal sum
            if root is None:
                return 
            func(root.left,True)
            func(root.right,False)
            if isleft:
                if root.left is None and root.right is None:
                    sum=sum+root.val

        func(root,False)
        return sum