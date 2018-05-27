/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func removeNthFromEnd(head *ListNode, n int) *ListNode {
    node := head
    i := 0
    var prev *ListNode = nil
    for node != nil {
        if i > n {
            prev = prev.Next
        } else if i == n {
            prev = head
        }
        node = node.Next
        i++
    }
    if prev == nil {
        head = head.Next
    } else {
        prev.Next = prev.Next.Next
    }
    return head
}
