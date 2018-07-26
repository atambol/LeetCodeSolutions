/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func rightSideView(root *TreeNode) []int {
    if root == nil {
        return []int{}
    }
    
    var depth []int
    var stack []*TreeNode
    var view []int
    var d int
    var D int
    view = append(view, root.Val)
    stack, depth = push(stack, root.Left, depth, d+1)
    node := root.Right
    d++
    
    for len(stack) != 0 || node != nil {
        if node == nil {
            stack, node, depth, d = pop(stack, depth)
        } else {
            if d > D {
                view = append(view, node.Val)
                D++
            }
            if node.Left != nil {
                stack, depth = push(stack, node.Left, depth, d+1)
            }
            node = node.Right
            d++
        }
    }
    return view
}

func push(stack []*TreeNode, node *TreeNode, depth []int, d int) ([]*TreeNode, []int) {
    stack = append(stack, node)
    depth = append(depth, d)
    return stack, depth
}

func pop(stack []*TreeNode, depth []int) ([]*TreeNode, *TreeNode, []int, int) {
    l := len(stack)-1
    node := stack[l]
    stack = stack[:l]
    d := depth[l]
    depth = depth[:l]
    return stack, node, depth, d
}
