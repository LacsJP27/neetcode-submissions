# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        # dummy node needed to return result and to get left at the parent index of the removed node
        left = dummy
        right = head
        
        # make a gap of size n + 1 (dummy L makes it + 1) to get left at the node before the node we want to remove
        while n > 0 and right:
            right = right.next
            n -=1

        # go until right reaches the end of the list then left is the parent of the node we want to remove
        while right:
            left = left.next
            right = right.next
        
        # deleting a node
        left.next = left.next.next

        return dummy.next # the head of the list
                




        


            