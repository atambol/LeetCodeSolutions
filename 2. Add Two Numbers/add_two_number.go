/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
import "fmt"

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
    head := new(ListNode)
    l3 := head
    carry := 0
    for {
        // Initiliase the node
        l3.Val = carry
        carry = 0
        
        // Assign appropriate values
        if l1 != nil {
            l3.Val += l1.Val
            l1 = l1.Next
        }
        if l2 != nil {
            l3.Val += l2.Val
            l2 = l2.Next
        }
        if l3.Val >= 10 {
            carry = l3.Val / 10
            l3.Val = l3.Val % 10
        }
        
        // Iterate or exit appropriately
        if l1 != nil || l2 != nil || carry != 0{
            l3.Next = new(ListNode)
            l3 = l3.Next
        } else {
            l3.Next = nil
            return head
        }
    }
}
