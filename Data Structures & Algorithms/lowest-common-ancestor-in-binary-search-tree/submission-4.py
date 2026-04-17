# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        maxNode = max(p.val, q.val)
        minNode = min(p.val, q.val)
        def dfs(node):
            if maxNode < node.val:
                return dfs(node.left)
            elif minNode > node.val:
                return dfs(node.right)
            return node
        return dfs(root)