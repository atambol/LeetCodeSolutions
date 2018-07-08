/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func levelOrder(root *TreeNode) [][]int {
    var sol [][]int
    if root == nil {
        return sol
    }
    var queue [](*TreeNode) // queue to maintain the elements to be covered in current level
    current_index := 0      // Manipulate indices of the slice queue to remember current level
    next_index := 1
    queue = append(queue, root)
    
    for next_index - current_index != 0 {
        var intermediate_sol []int
        tmp := next_index
        for i := current_index; i < next_index; i++ {
            intermediate_sol = append(intermediate_sol, queue[i].Val)
            if queue[i].Left != nil {
                queue = append(queue, queue[i].Left)
                tmp++
            }
            if queue[i].Right != nil {
                queue = append(queue, queue[i].Right)
                tmp++
            }
        }
        current_index = next_index
        next_index = tmp
        fmt.Println(intermediate_sol)
        sol = append(sol, intermediate_sol)
    }
    return sol
}
