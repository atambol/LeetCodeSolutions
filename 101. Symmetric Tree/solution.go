/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isSymmetric(root *TreeNode) bool {
    if root == nil {
        return true
    }
    
    return isSymmetry(root.Left, root.Right)
}

func isSymmetry(a *TreeNode, b *TreeNode) bool {
    if a == nil && b != nil {
        return false
    } else if a != nil && b == nil {
        return false
    } else if a == nil && b == nil {
        return true
    } else if a.Val != b.Val {
        return false
    } else {
        return (isSymmetry(a.Left, b.Right) && isSymmetry(b.Left, a.Right))
    }
}
