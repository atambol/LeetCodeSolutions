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
        // edge cases
        if (head == null || head.next == null) {
            return head;
        } 
        
        if (m == n) {
            return head;
        }
        
        // add a dummy head
        ListNode node = new ListNode(0);
        node.next = head;
        head = node;
        ListNode tail1, tmp, tail2, prev;
        prev = node;
        node = node.next;
        
        // reach mth node
        while (m != 1) {
            m--;
            n--;
            prev = node;
            node = node.next;
        }
        
        tail1 = prev;
        tail2 = node;
        
        // reverse until nth node
        prev = null;
        while (n != 0) {
            n--;
            tmp = node.next;
            node.next = prev;
            prev = node;
            node = tmp;
        }
        
        // attach the three parts
        tail2.next = node;
        tail1.next = prev;
        
        return head.next;
    }
}
