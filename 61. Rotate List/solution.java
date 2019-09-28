/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        // edge cases
        if (k == 0) {
            return head;
        }
        
        if (head == null || head.next == null) {
            return head;
        }
        
        // find length of the list
        int len = 0;
        ListNode node = head;
        while (node != null) {
            len++;
            node = node.next;
        }
        
        k = k%len;
        
        if (k == 0) {
            return head;
        }
        
        ListNode prev = head;
        node = head;
        while (k > 0) {
            node = node.next;
            k--;
        }
        
        while (node.next != null) {
            prev = prev.next;
            node = node.next;
        }
        
        node.next = head;
        node = prev.next;
        prev.next = null;
        return node;
    }
}
