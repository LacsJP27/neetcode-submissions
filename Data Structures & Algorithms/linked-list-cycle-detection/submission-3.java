/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public boolean hasCycle(ListNode head) {
        // Set<ListNode> nodeSet = new HashSet<>();
        // while(head != null){
        //     if(nodeSet.contains(head)) return true;
        //     nodeSet.add(head);
        //     head = head.next;
        // }

        // return false; O(n) extra space and O(1) time to detect duplicates

        ListNode slow = head;
        if(head.next == null) return false; 
        ListNode fast = head.next.next;

        while(slow != null && fast != null){
            if(slow == fast) return true;
            slow = slow.next;
            fast = fast.next.next;
        }

        return false;
        
    }
}
