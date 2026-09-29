# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: TreeNode | None) -> int:
        q=deque()
        q.append((root,0))
        maxwidth=0
        while q:
            n=len(q)
            fp=q[0][1]
            for i in range(n):
                node=q.popleft()
                lp=node[1]

                if node[0].left !=None:
                    q.append((node[0].left,2*node[1]))
                if node[0].right !=None:
         
                    q.append((node[0].right,2*node[1]+1))
            maxwidth=max(maxwidth,lp-fp+1)

        return maxwidth

