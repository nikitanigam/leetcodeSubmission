# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        q=deque()
        ans=[]
        if root is None:
            return ans 
        q.append(root)
        d=False
        while(q):
            n=len(q)
            l=[]
            for i in range(n):
                node=q.popleft()
                l.append(node.val)
                if node.left!=None:
                    q.append(node.left)
                if node.right!=None:
                    q.append(node.right)
            if d==True:
                l.reverse()
                ans.append(l)
            else:
                ans.append(l)
            if d==False:
                d=True
            else:
                d=False

        return ans 


        