# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def ismirror(left,right)->bool:
            if left is None and right is None:
                return True
            if left is None:
                return False
            if right is None:
                return False
            if left.val!=right.val:
                return False

            return ismirror(left.left,right.right) and ismirror(left.right,right.left)
        leftroot=root.left
        rightroot=root.right
        return ismirror(leftroot,rightroot)
        
            
        