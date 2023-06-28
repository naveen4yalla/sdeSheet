class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []  # create a heap
        new_list = ListNode()  # dummy node
        
        counter = 0  # This counter is to add an abitrary value to the heap more below
        '''
        We will be passing a tuple into the queue. Originally, I wanted to do heap.push((node.val, node))
        But in this case, we'll get a runtime error. heapq uses the first item of an inserted tuple. If two tuples are inserted,
        it compares by the next item in the tuple. (1, node1) and (1, node2) will generated a TypeError. This is becuase the node
        class Leetcode provided does not have a __lt__ function, that is, nodes can't be compared! We remedy this by setting a counter
        as the second item in our tuple. So instead of (node.val, node), we will input (node.val, counter, node) then increment the counter.
        This way, if two nodes have the same val, we get the one that entered the heap first, which will have a lower counter val. 
        In any case if we have items like this in there: (1, 0, node1), (2, 1, node), (-1, 3, node), when we pop, we will get in order:
        (-1, 3, node), (1, 0, node1), (2, 1, node). So regardless the counter value, we will get the smallest items first! The counter is more
        like the priorit in which we get them! Hope that made sense!
        '''
        for linked_list in lists:
            if not linked_list:
                continue
            
            # push all head nodes in our priority queue
            list_val = linked_list.val
            heapq.heappush(heap, (list_val, counter, linked_list))
            counter += 1
        
        # If we have an empty heap after pushing all heads, that means there are no nodes at all!
        if not heap:
            return None
        
        # keep popping out of the heap
        cur_node = new_list
        while heap:
            node_tuple = heapq.heappop(heap)
            node = node_tuple[2]
            node_next = node.next
            cur_node.next = node
            cur_node = cur_node.next
            
            # whichever node was the smallest, its next will be added to the heap, if it is not null
            if node_next:
                list_val = node_next.val
                new_node_tuple = (list_val, counter, node_next)
                heapq.heappush(heap, new_node_tuple)
                counter += 1
        
        # get the dummy node's next. Which is the head
        return new_list.next