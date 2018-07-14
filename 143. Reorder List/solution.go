/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reorderList(head *ListNode)  {
    // Edge cases
    if head == nil || head.Next == nil  || head.Next.Next == nil {
        return
    }
    
    // Get to the middle of the linkedlist
    slowRunner, fastRunner := head, head
    var prev *ListNode
    for fastRunner != nil && fastRunner.Next != nil {
        fastRunner = fastRunner.Next.Next
        prev = slowRunner
        slowRunner = slowRunner.Next
    }
    
    // detach the second half
    head2 := slowRunner
    prev.Next = nil
    
    // reverse the second half of the list
    node := head2.Next
    prev = head2
    prev.Next = nil
    for node != nil {
        tmp := node.Next
        node.Next = prev
        prev = node
        node = tmp
    } 
    head2 = prev
    
    // interleave the first half and the reversed second half
    node1 := head.Next
    node2 := head2
    node = head
    
    for node1 != nil || node2 != nil {
        if node2 != nil {
            node.Next = node2
            node2 = node2.Next
            node = node.Next
        }
        
        if node1 != nil {
            node.Next = node1
            node1 = node1.Next
            node = node.Next
        }
    }
    node.Next = nil
    
    return
}
