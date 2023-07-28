class ListNode:
    def __init__(self,key):
        self.key = key
        self.next = None
        
class MyHashSet:

    def __init__(self):
        self.size = 1069
        self.bucket = [ListNode(-1) for i in range(self.size)]
        

    def add(self, key: int) -> None:
        hasher = key % self.size
        head = self.bucket[hasher]
        curr = head.next
        while curr:
            if curr.key == key:return
            head = curr
            curr = curr.next
        curr = ListNode(key)
        head.next = curr
       
            
        
    def remove(self, key: int) -> None:
        hasher = key % self.size
        head = self.bucket[hasher]
        curr = self.bucket[hasher].next
        while curr:
            if curr.key == key:
                head.next = head.next.next
            head = curr
            curr = curr.next
        
                
    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        hasher = key % self.size
        curr = self.bucket[hasher]
        while curr :
            if curr.key == key:
                return True
            curr = curr.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)