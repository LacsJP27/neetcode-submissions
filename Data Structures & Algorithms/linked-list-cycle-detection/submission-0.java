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
        ListNode node = head;
        ArrayList<Integer> visited = new ArrayList<Integer>(10);
        while(node.next != null){
            if(visited.contains(node.val)){
                return true;
            }
            visited.add(node.val);
            node = node.next;
        }
        return false;
    }
}
