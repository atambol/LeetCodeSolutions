/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode reverseBetween(ListNode head, int m, int n) {
        // insert dummy node
        ListNode node = new ListNode(0);
        node.next = head;
        head = node;
        
        // arrive at the mth node
        ListNode prev = head;
        node = head.next;
        
        while (m > 1) {
            m--;
            n--;
            prev = node;
            node = node.next;
        }
        
        // reverse m-n nodes
        ListNode tail = prev;
        ListNode head2 = node;
        ListNode tmp;
        prev = null;
        while (n > 0) {
            n--;
            tmp = node.next;
            node.next = prev;
            prev = node;
            node = tmp;
        }
        
        // reattach and return
        tail.next = prev;
        head2.next = node;
        return head.next;
    }
}
