# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        # have a queue for each level
        # pop the queue into result for each level until empty
        # and then move onto the next level
        # [4, 5, 6, 7]
        queue = collections.deque()
        queue.append(root)
        while queue:

            qlen = len(queue)
            level = []
            for i in range(qlen):
                node = queue.popleft()
                if node:
                    queue.append(node.left)
                    queue.append(node.right)
                    level.append(node.val)
            if level:
                res.append(level)

        return res

            