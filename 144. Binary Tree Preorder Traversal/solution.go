/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func preorderTraversal(root *TreeNode) []int {
    if root != nil {
        output := []int{root.Val}
        output = append(output, preorderTraversal(root.Left)...)
        output = append(output, preorderTraversal(root.Right)...)
        return output
    } else {
        return []int{}
    }
}
