# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestorBT(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # the root is an ancestor if right and left have p and q
        # the second p and q or on right or left then we split
        # it's impossible for to go lower and be a common ancestor
        # this is for BT
        # for a BST we con do something differ

        if (self.containsNode(root.left, p) and self.containsNode(root.left, q)):
            return self.lowestCommonAncestor(root.left, p, q)
        if self.containsNode(root.right, p) and self.containsNode(root.right, q):
            return self.lowestCommonAncestor(root.right, p, q) 
        else:
            return root

    def containsNode(self, root: TreeNode, target: TreeNode) -> bool:
        if root == None: return False

        if root.val == target.val: return True

        return self.containsNode(root.right, target) or self.containsNode(root.left, target)

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if (q.val <= root.val and p.val >= root.val) or (q.val >= root.val and p.val <= root.val):
            return root
        if root.val < max(q.val, p.val):
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return self.lowestCommonAncestor(root.left, p, q)
