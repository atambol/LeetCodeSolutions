/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func max(a, b int) int {
    if b > a {
        return b
    } else {
        return a
    }
}

func longestConsecutive(root *TreeNode) int {
    if root == nil {
        return 0
    } 
    currentLongest, lastLongest := bst(root)
    return max(currentLongest, lastLongest)
}

func bst(root *TreeNode) (int, int) {
    leftCurrentLongest, rightCurrentLongest, leftLastLongest, rightLastLongest := 1, 1, 0, 0
    
    if root.Left != nil {
        leftCurrentLongest, leftLastLongest = bst(root.Left)
        if root.Left.Val == root.Val + 1 {
            leftCurrentLongest++
        } else {
            leftLastLongest = max(leftCurrentLongest, leftLastLongest)
            leftCurrentLongest = 1
        }
    } 
    
    if root.Right != nil {
        rightCurrentLongest, rightLastLongest = bst(root.Right)
        if root.Right.Val == root.Val + 1 {
            rightCurrentLongest++
        } else {
            rightLastLongest = max(rightCurrentLongest, rightLastLongest)
            rightCurrentLongest = 1
        }
    }
    
    return max(leftCurrentLongest, rightCurrentLongest), max(leftLastLongest, rightLastLongest)
}32
