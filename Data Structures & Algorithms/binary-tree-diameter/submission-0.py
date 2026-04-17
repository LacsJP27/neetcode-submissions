# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # have a current max
        # have current max path
        # take the max of the left path plus the max of the right path
        # set it as current max if greater
        # when returning up to parent make sure to only return the path
        res = 0

        def dfs(node):
            nonlocal res

            if not node:
                return 0
            
            right = dfs(node.right)
            left = dfs(node.left)
            # this checks if going down right and left subtrees 
            # have a greater combined path then current max
            res = max(res, left + right)

            # return only the longest of two paths
            # can't count a node twice
            return 1 + max(left, right)            
            
        dfs(root)
        return res

