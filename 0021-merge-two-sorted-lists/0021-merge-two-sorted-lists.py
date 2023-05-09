class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        res = n = ListNode(0)
        
        while l1 and l2:
            if l1.val < l2.val :
                x = ListNode(l1.val)
                l1 = l1.next
            else:
                x = ListNode(l2.val)
                l2 = l2.next
                
            res.next = x
            res = res.next
            
        if l1:
            res.next = l1
            
        if l2:
            res.next = l2
            
        # res = res.next
        return n.next