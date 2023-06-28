from queue import PriorityQueue

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = point = ListNode(0)
        q = PriorityQueue()
        c = 1
        for l in lists:
            if l:
                q.put((l.val,c, l))
                c += 1
        while not q.empty():
            val,index , node = q.get()
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                q.put((node.val,c, node))
                c += 1
        return head.next