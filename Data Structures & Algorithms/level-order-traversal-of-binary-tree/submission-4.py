# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = collections.deque()
        queue.append(root) #root = 1
        while queue:
            qlen = len(queue) #1, 2
            level = []

            for i in range(qlen):
                node = queue.popleft() # 1, 2, 3, 4
                if node:
                    queue.append(node.left) # queue: 2, 3; 3, 4, 5; 4, 5, 6, 7; 5, 6, 7,None, NOne
                    queue.append(node.right)
                    level.append(node.val) # [1], [2, 3]
            if level:
                res.append(level) # [[1]. [2, 3]]
        
        return res
            