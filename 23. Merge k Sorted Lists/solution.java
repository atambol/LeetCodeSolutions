/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        ListNode head = new ListNode(0);
        ListNode node = head;
        int low = 0;
        int min;
        while (true) {
            low = -1;
            min = Integer.MAX_VALUE;
            for(int i = 0; i < lists.length; i++) {
                if (lists[i] != null && lists[i].val < min) {
                    low = i;
                    min = lists[i].val;
                }
            }
            if (low == -1) {
                return head.next;
            }
            node.next = lists[low];
            lists[low] = lists[low].next;
            node = node.next;
        }
    }
}
