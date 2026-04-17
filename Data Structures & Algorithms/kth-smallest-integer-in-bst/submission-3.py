# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # you actually don't need to iterate through a stack
        # just in order traversal and take the element k - 1 will give you kth smallest
        arr = []

        def dfs(node):
            if not node:
                return

            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)

        dfs(root)
        return arr[k - 1]

    def kthSmallestMyVersion(self, root: Optional[TreeNode], k: int) -> int:
        # go to the biggest node
        # put at the bottom of the stack
        # go to the next biggest
        # add to stack
        # pop stack k times to get the kth smallest node'
        stack = []
        def dfs(node):
            if not node:
                return
            dfs(node.right)
            stack.append(node)
            dfs(node.left)
        dfs(root)
        for i in range(k):
            if stack:
                res = stack.pop()
        return res.val
                
