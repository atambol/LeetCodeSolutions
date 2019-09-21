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
        ListNode head = new ListNode(Integer.MIN_VALUE);
        ListNode node = head;
        PriorityQueue<ListNode> heap = new PriorityQueue<>(11, (x, y) -> x.val - y.val);
        for(ListNode nodes: lists) {
            while (nodes != null) {
                node = nodes;
                nodes = nodes.next;
                node.next = null;
                heap.add(node);
            }
        }
        
        node = head;
        while (node != null) {
            node.next = heap.poll();
            node = node.next;
        }
        
        return head.next;
    }
}
