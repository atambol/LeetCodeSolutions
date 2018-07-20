/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func removeElements(head *ListNode, val int) *ListNode {
    var prev *ListNode
    curr := head
    for curr != nil {
        if curr.Val == val {
            if prev == nil {
                head = head.Next
                curr = head
            } else {
                prev.Next = curr.Next
                curr = curr.Next
            }
        } else {
            prev = curr
            curr = curr.Next
        }
    }
    return head
}
