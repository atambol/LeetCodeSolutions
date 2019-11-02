/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode plusOne(ListNode head) {
        // reverse list
        head = reverse(head);
        
        // add one
        int carry = 1;
        ListNode node = head;
        ListNode prev = null;
        while (node != null && carry != 0) {
            node.val += carry;
            if (node.val > 9) {
                node.val %= 10;
            } else {
                carry = 0;
            }
            prev = node;
            node = node.next;
        }
        
        if (carry != 0) {
            prev.next = new ListNode(carry);
        }
        
        // reverse
        return reverse(head);
    }
    
    public ListNode reverse(ListNode head) {
        ListNode node, prev, tmp;
        prev = null;
        node = head;
        while (node != null) {
            tmp = node.next;
            node.next = prev;
            prev = node;
            node = tmp;
        }
        head = prev;
        return head;
    }
}
