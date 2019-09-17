/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode head = new ListNode(0);
        ListNode node = head;
        int carry = 0;
        
        while (l1 != null && l2 != null) {
            node.next = new ListNode(carry);
            carry = 0;
            node = node.next;
            node.val += l1.val + l2.val;
            if (node.val > 9) {
                carry = 1;
                node.val %= 10;
            }
            l1 = l1.next;
            l2 = l2.next;
        }
        
        while (l1 != null) {
            node.next = new ListNode(carry);
            carry = 0;
            node = node.next;
            node.val += l1.val;
            if (node.val > 9) {
                carry = 1;
                node.val %= 10;
            }
            l1 = l1.next;
        }
        
        while (l2 != null) {
            node.next = new ListNode(carry);
            carry = 0;
            node = node.next;
            node.val += l2.val;
            if (node.val > 9) {
                carry = 1;
                node.val %= 10;
            }
            l2 = l2.next;
        }
        
        if (carry == 1) {
            node.next = new ListNode(carry);
        }
        
        return head.next;
    }
}
