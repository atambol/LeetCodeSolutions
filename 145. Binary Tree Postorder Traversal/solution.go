/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func postorderTraversal(root *TreeNode) []int {
    if root != nil {
        output := postorderTraversal(root.Left)
        output = append(output, postorderTraversal(root.Right)...)
        output = append(output, root.Val)
        return output
    } else {
        return []int{}
    }
}
