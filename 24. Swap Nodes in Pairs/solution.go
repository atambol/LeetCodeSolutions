/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func swapPairs(head *ListNode) *ListNode {
    if head == nil || head.Next == nil {
        return head
    }
    
    prev := head
    cur := head.Next
    
    head = cur
    node := cur.Next
    cur.Next = prev
    prev.Next = node
    cur = node
    for cur != nil && cur.Next != nil {
        node = cur.Next
        cur.Next = node.Next
        prev.Next = node
        node.Next = cur
        
        prev = cur
        cur = prev.Next
        
    }
    return head
}
