# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        queue = deque()
        queue.append(root)
        while queue:
            qlen = len(queue) # 1
            node = None
            for i in range(qlen): #queue: [1], [2, 3], [3, 4], [4]
                node = queue.popleft() # 1; 2, 3; 
                if node:
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            if node:
                res.append(node.val) #1, 3
        return res