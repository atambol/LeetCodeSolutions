/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reverseList(head *ListNode) *ListNode {
    var tail *ListNode
    newHead := reverse(head, tail)
    return newHead
}

func reverse(head *ListNode, tail *ListNode) (*ListNode) {
    if head == nil {
        return tail
    } else {
        node := head
        head = head.Next
        node.Next = tail
        tail = node
        return reverse(head, tail)
    }
}
