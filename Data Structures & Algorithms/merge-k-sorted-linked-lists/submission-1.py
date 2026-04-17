# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodeArr = [] 
        for node in lists:
            nodeArr.append(node)
        minNode = float('-inf')
        res = ListNode()
        node = res
        validNodes = [n for n in nodeArr if n is not None]
        minNode = min(validNodes, key=lambda n: n.val) if validNodes else None
        while minNode:
            node.next = minNode
            node = node.next
            # update the nodeArr to remove the minNode
            nodeArr[nodeArr.index(minNode)] = minNode.next
            validNodes = [n for n in nodeArr if n is not None]
            minNode = min(validNodes, key=lambda n: n.val) if validNodes else None
        return res.next















    def mergeKListsBruteForce(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
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
        
