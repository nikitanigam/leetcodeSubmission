# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    from collections import deque
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=deque()
        ans=[]
        if root is None:
            return ans
        
        q.append(root)
        while(len(q)>0):
            l=[]
            for i in range(len(q)):
                a=q.popleft()
                l.append(a.val)
                if a.left is not None:
                    q.append(a.left)
                if a.right is not None:
                    q.append(a.right)
            ans.append(l)
        return ans
            




        