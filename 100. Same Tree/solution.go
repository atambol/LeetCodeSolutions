/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isSameTree(p *TreeNode, q *TreeNode) bool {
    str1 := inorder(p)
    str2 := inorder(q)
    fmt.Println(str1, str2)
    return compare(str1, str2)
}

func inorder(p *TreeNode) string {
    if p != nil {
        return string(p.Val) + inorder(p.Left) + inorder(p.Right)
    } else {
        return "n"
    }
}

func compare(str1 string, str2 string) bool {
    if len(str1) != len(str2) {
        return false
    }

    for i:=0; i<len(str1); i++ {
        if str1[i] != str2[i] {
            return false
        }
    }
    return true
}
