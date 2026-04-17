# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodeArr = []
        for node in lists:
            while node:
                nodeArr.append(node.val)
                node = node.next
        res = ListNode()
        curr = res
        nodeArr = sorted(nodeArr)
        for val in nodeArr:
            curr.next = ListNode(val)
            curr = curr.next
        return res.next
        
