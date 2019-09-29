/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

// time complexity is nlogn (assuming that left and right subtree are same in size)
// getIndex would find root at the center of each inorder tree
// thus for each iteration the linear search would have complexity of n/2
// n/2 + n/4 + n/8 .. = nlogn
// https://stackoverflow.com/questions/5585928/time-complexity

class Solution {
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        return reconstructTree(preorder, 0, preorder.length-1,
                               inorder, 0, inorder.length-1);
    }
    
    public TreeNode reconstructTree(int[] preorder, int pre_i, int pre_j,
                                   int[] inorder, int in_i, int in_j) {
        if (pre_i > pre_j) {
            return null;
        } else if (pre_i == pre_j) {
            return new TreeNode(preorder[pre_i]);
        } else {
            TreeNode root = new TreeNode(preorder[pre_i]);
            int root_pos_in_inorder = getIndex(inorder, in_i, in_j, preorder[pre_i]);
            if (root_pos_in_inorder == in_i) {
                root.right = reconstructTree(preorder, pre_i+1, pre_j,
                               inorder, in_i+1, in_j);
            } else if (root_pos_in_inorder == in_j) {
                root.left = reconstructTree(preorder, pre_i+1, pre_j,
                               inorder, in_i, in_j-1);
            } else {
                int element_count_in_left_subtree = root_pos_in_inorder - in_i;

                root.left = reconstructTree(preorder, pre_i + 1, pre_i + element_count_in_left_subtree,
                               inorder, in_i, root_pos_in_inorder-1);
                root.right = reconstructTree(preorder, pre_i + element_count_in_left_subtree + 1, pre_j,
                               inorder, root_pos_in_inorder + 1, in_j);
            }
            return root;
        }
    }
    
    public int getIndex(int[] arr, int start, int end, int val) {
        for (int i = start; i <= end; i++) {
            if (arr[i] == val) {
                return i;
            }
        }
        return -1;
    }
}
