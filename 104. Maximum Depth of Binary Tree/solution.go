/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func maxDepth(root *TreeNode) int {
    if root == nil {
        return 0
    } else {
        leftD := maxDepth(root.Left)
        rightD := maxDepth(root.Right)
        if leftD > rightD {
            return 1 + leftD
        } else {
            return 1 + rightD
        }
    }
}
