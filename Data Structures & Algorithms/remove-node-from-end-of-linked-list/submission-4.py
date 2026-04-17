# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        linkedList = []
        node = head
        while node:
            linkedList.append(node)
            node = node.next
        dummy = ListNode()
        curr = dummy
        fromEnd = len(linkedList) - n
        for i in range(len(linkedList)):
            if i == fromEnd:
                continue
            print(linkedList[i].val)
            curr.next = linkedList[i]
            curr = curr.next
        
        curr.next = None
        return dummy.next

                




        


            