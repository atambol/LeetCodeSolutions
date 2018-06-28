/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func deleteDuplicates(head *ListNode) *ListNode {
    var prev *ListNode
    cur := head
    for cur != nil {
        if prev != nil && prev.Val == cur.Val {
            prev.Next = cur.Next
        } else {
            prev = cur  
        }
       
        cur = cur.Next
    }
    return head
}
