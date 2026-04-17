# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEndBruteForce(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
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
            curr.next = linkedList[i]
            curr = curr.next
        # must reset if the last node is the node being removed
        # otherwise it's old next value will still be there
        curr.next = None
        return dummy.next
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        # dummy node needed to return result and to get left at the parent index of the removed node
        left = dummy
        right = head
        while n > 0 and right:
            right = right.next
            # this will put right where the nth position from the end is
            n -= 1
        # move right to the end of the list and move left to the parent of the node we want to remove
        while right:
            left = left.next
            right = right.next
        
        left.next = left.next.next

        return dummy.next
        
        


                




        


            