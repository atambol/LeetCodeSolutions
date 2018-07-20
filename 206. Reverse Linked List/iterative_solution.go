/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reverseList(head *ListNode) *ListNode {
    curr := head
    var tail *ListNode
    for curr != nil {
        tmp := curr
        curr = curr.Next
        tmp.Next = tail
        tail = tmp
    }
    return tail
}
