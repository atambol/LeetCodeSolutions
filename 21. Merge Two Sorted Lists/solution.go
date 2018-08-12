/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func mergeTwoLists(l1 *ListNode, l2 *ListNode) *ListNode {
    var head, node *ListNode
    
    for l1 != nil && l2 != nil {
        if l1.Val > l2.Val {
            if node != nil {
                node.Next = l2
                node = node.Next
                l2 = l2.Next
                node.Next = nil
            } else {
                head = l2
                node = l2
                l2 = l2.Next
            }
        } else {
            if node != nil {
                node.Next = l1
                node = node.Next
                l1 = l1.Next
                node.Next = nil
            } else {
                head = l1
                node = l1
                l1 = l1.Next
            }

        }
    }
    
    if l1 != nil {
        if node == nil {
            return l1
        } else {
            node.Next = l1
        }
    } else if l2 != nil {
        if node == nil {
            return l2
        } else {
            node.Next = l2
        }
    }
    
    return head
}
