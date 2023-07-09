# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        #Base condition to check
        if not head: return None
        curr = head
        #fix the left position 
        l = left
        r = right
        curr , prev = head , None
        while l > 1:
            prev = curr
            curr = curr.next
            l = l-1
            r = r-1
        tail = curr
        con = prev
        
        while r:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            r-=1
        if con:
            con.next = prev
        else:
            head = prev
        tail.next = curr
        return head
            
            
        
        