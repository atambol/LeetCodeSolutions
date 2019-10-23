/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode detectCycle(ListNode head) {
        if (head == null || head.next == null) {
            return null;
        }
        
        ListNode sptr = head;
        ListNode fptr = head;
        
        while (fptr != null && fptr.next != null) {
            fptr = fptr.next.next;
            sptr = sptr.next;
            if (fptr == sptr) {
                break;
            }
        }

        if (fptr == null || fptr.next == null) {
            return null;
        }

        sptr = head;
        while (sptr != fptr) {
            fptr = fptr.next;
            sptr = sptr.next;
        }
        
        return sptr;
    }
}
