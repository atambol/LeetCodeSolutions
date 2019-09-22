/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        // Count the number of iterations required
        int groupCount = 0;
        ListNode node = head;
        while (node != null) {
            groupCount += 1;
            node = node.next;
        }
        groupCount /= k;
        
        // Reverse nodes in groups of k
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prev = null;
        node = head;
        ListNode tail1 = dummy;
        ListNode tail2 = node;
        ListNode tmp;
        while (groupCount != 0) {
            for (int i = 0; i < k; i++) {
                tmp = node.next;
                node.next = prev;
                prev = node;
                node = tmp;
            }
            tail1.next = prev;
            tail1 = tail2;
            prev = null;
            tail2 = node;
            groupCount--;
        }
        tail1.next = node;
        return dummy.next;
    }
}
