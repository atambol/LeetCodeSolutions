/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func insertionSortList(head *ListNode) *ListNode {
    if head == nil || head.Next == nil {
        return head
    }
    curr1 := head.Next
    prev1 := head
    for curr1 != nil {
        curr2 := head
        var prev2 *ListNode
        
        // Identify the sorted position for this element (runner)
        for curr2 != curr1 {
            if curr2.Val > curr1.Val {
                break
            } else {
                prev2 = curr2
                curr2 = curr2.Next
            }
        }
        
        if curr2 == curr1 {
            // The element is already in correct position
            prev1 = curr1
            curr1 = curr1.Next
        } else {
            // move the element pointed to by runner to the above position
            tmp := curr1.Next
            prev1.Next = tmp
            
            if prev2 == nil {
                curr1.Next = head
                head = curr1
            } else {
                prev2.Next = curr1
                curr1.Next = curr2
            }
            
            curr1 = tmp
        }
    }
    return head
}
