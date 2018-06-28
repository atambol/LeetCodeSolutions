func isValidBST(root *TreeNode) bool {
    if root == nil {
        return true
    }
    
    // Get the inorder traversal
    list := inorder(root)
    
    // Check if the elements in the list are sorted in increasing order
    for i:=0; i<len(list)-1;i++{
        if list[i] >= list[i+1] {
            return false
        }
    }
    return true
}

func inorder(root *TreeNode) []int {
    if root.Left == nil && root.Right == nil {
        return []int{root.Val}
    } else if root.Left != nil && root.Right == nil {
        left := inorder(root.Left)
        return append(left, root.Val)
    } else if root.Left == nil && root.Right != nil {
        right := inorder(root.Right)
        return append([]int{root.Val}, right...)
    } else {
        left := inorder(root.Left)
        right := inorder(root.Right)
        return append(left, append([]int{root.Val}, right...)...)
    } 
}
