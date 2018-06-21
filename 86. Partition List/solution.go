func partition(head *ListNode, x int) *ListNode {
    if head == nil || head.Next == nil {
        return head
    }
    
    var prev, shead, lhead, stail *ListNode

    //Traverse until the first node with val >= x appears
    node := head
    for node != nil && node.Val < x {
        prev = node
        node = node.Next
    }
    
    if node == nil { // All nodes are less than x
        return head
    } else {    // Split the list into two lists
        if prev == nil {
            shead = nil
            stail = nil
            lhead = head
        } else {
            shead = head
            stail = prev
            stail.Next = nil 
            lhead = node
        }
    }
    
    // Remove nodes from large list that have val<x and append them to small list
    node = lhead
    prev = nil
    for node != nil {
        if node.Val < x {
            // Detach
            if prev != nil {
                prev.Next = node.Next
            } else {
                lhead = lhead.Next
            }
            
            // Attach
            if stail == nil {
                stail = node
                shead = node
            } else {
                stail.Next = node
                stail = stail.Next
            }
            node.Next = nil
            
            //Increment
            node = prev.Next
        } else {
            prev = node
            node = node.Next
        }
    }
    
    // Join the two lists and return
    if stail != nil {
        stail.Next = lhead
        return shead
    } else {
        return lhead
    }
}
