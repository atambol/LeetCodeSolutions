/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reverseBetween(head *ListNode, m int, n int) *ListNode {
    // edge cases
    if m == n || head == nil || head.Next == nil {
        return head
    }
    
    // Arrive at the reversal point
    var prev *ListNode
    curr := head
    for i:=1; i<m; i++ {
        prev = curr
        curr = curr.Next
    }
    
    tail1 := prev
    
    // Reverse the linked list
    var head2 *ListNode
    var tail2 *ListNode
    prev = nil
    for i:=m; i<=n; i++ {
        if tail2 == nil {
            tail2 = curr
        }
        tmp := curr.Next
        curr.Next = head2
        head2 = curr
        curr = tmp
    }
    
    // Reversing from the head
    if tail1 == nil {
        tail2.Next = curr
        return head2
    } else {    // Reversing from the middle
        tail1.Next = head2
        tail2.Next = curr    
    }
    
    return head
}
