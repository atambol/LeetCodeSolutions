/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func inorderTraversal(root *TreeNode) []int {
    if root != nil {
        output := inorderTraversal(root.Left)
        output = append(output, root.Val)
        output = append(output, inorderTraversal(root.Right)...)
        return output
    } else {
        return []int{}
    }
}
