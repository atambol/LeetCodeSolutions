/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func deleteDuplicates(head *ListNode) *ListNode {
    var prev *ListNode
    cur := head
    
    // Remove all the repeats except for the first occurance and remember the repeated numbers
    repeats := make(map[int]bool)
    for cur != nil {
        if prev != nil && prev.Val == cur.Val {
            repeats[cur.Val] = true
            prev.Next = cur.Next
        } else {
            repeats[cur.Val] = false
            prev = cur  
        }
        cur = cur.Next
    }
    
    // Remove all the single occurence of repeated numbers
    for head != nil && repeats[head.Val] == true {
        head = head.Next
    }
    if head == nil {
        return head
    }
    prev = head
    cur = head.Next
    for cur != nil {
        if repeats[cur.Val] == true {
            prev.Next = cur.Next
        } else {
            prev = cur
        }
        cur = cur.Next
    }
    return head
}
