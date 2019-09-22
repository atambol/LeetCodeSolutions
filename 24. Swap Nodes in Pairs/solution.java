/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode swapPairs(ListNode head) {
        ListNode dummy = new ListNode(0);
        ListNode prev = dummy;
        ListNode node = head;
        dummy.next = head;
        ListNode tmp;
        
        while (node != null && node.next != null) {
            tmp = node.next;
            node.next = node.next.next;
            tmp.next = node;
            prev.next = tmp;
            prev = node;
            node = node.next;
        }
        return dummy.next;
    }
}
