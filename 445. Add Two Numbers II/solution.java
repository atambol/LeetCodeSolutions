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
        l1 = reverseList(l1);
        l2 = reverseList(l2);
        int carry = 0;
        
        ListNode node1 = l1;
        ListNode node2 = l2;
        ListNode prev = null;
        while (node1 != null && node2 != null) {
            node1.val += node2.val + carry;
            // carry = 0;
            carry = node1.val/10;
            node1.val %= 10;
            prev = node1;
            node1 = node1.next;
            node2 = node2.next;
        }
        
        if (node2 != null && prev != null) {
            prev.next = node2;
            node1 = node2;
        }
        
        while (node1 != null && carry > 0) {
            node1.val += carry;
            carry = node1.val/10;
            node1.val %= 10;
            prev = node1;
            node1 = node1.next;
        }
        
        if (carry > 0) {
            prev.next = new ListNode(carry);
        }
        
        return reverseList(l1);
    }
    
    public ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode tmp;
        
        while (head != null) {
            tmp = head.next;
            head.next = prev;
            prev = head;
            head = tmp;
        }
        
        return prev;
    }  
}
