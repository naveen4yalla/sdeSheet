# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #Find the tail of the linked list 
        if not head: return head
        tail = head 
        length = 1
        while tail.next:
            tail = tail.next
            length+=1
        #find the intersection
        #(length - k - 1)
        k = k%length
        curr = head
        if  k == 0: return head
        for i in range(length-k-1):
            curr = curr.next
        newhead = curr.next
        curr.next = None
        tail.next = head
        
        return newhead
            
        
        