/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {  
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        if((root == null && subRoot != null) || subRoot == null) return false;
        if(equalsTree(root,subRoot) || isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot)) return true;
         return false;

    }

    public boolean equalsTree(TreeNode root1, TreeNode root2) {
        if(root1 == null && root2 == null) return true;
        if(root1 == null && root2 != null || root1 != null && root2 == null) return false;
        if(root1.val == root2.val && equalsTree(root1.left, root2.left) 
        && equalsTree(root1.right, root2.right)) return true;

        return false;
    }
}
