/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode sptr, fptr;
        fptr = head;
        fptr = new ListNode(0);
        fptr.next = head;
        head = fptr;
        while (n >= 0) {
            fptr = fptr.next;
            n--;
        }
        
        sptr = head;
        while (fptr != null) {
            fptr = fptr.next;
            sptr = sptr.next;
        }
        
        sptr.next = sptr.next.next;
        return head.next;
    }
}
