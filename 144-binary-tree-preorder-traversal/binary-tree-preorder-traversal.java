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
    public void preorder(TreeNode node , List<Integer> lst){
        if(node == null){
            return;
        }
        lst.add(node.val);
        preorder(node.left,lst);
        preorder(node.right,lst);

    }
    public List<Integer> preorderTraversal(TreeNode root) {

        List <Integer> lst = new ArrayList <>();

        preorder(root,lst);
        return lst;

        
        
    }
}