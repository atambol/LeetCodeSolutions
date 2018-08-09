/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func mergeTrees(t1 *TreeNode, t2 *TreeNode) *TreeNode {
    if t1 != nil && t2 != nil {
        t1.Val = t1.Val + t2.Val
        t1.Left = mergeTrees(t1.Left, t2.Left)
        t1.Right = mergeTrees(t1.Right, t2.Right)
        return t1
    } else if t1 != nil && t2 == nil {
        return t1
    } else if t1 == nil && t2 != nil {
        return t2
    } else {
        return t1
    }
}
