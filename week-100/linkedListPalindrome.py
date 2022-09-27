class Node:
    def __init__(self,data):
        self.val = data
        self.next =None
class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    def addAtHead(self,val):
        self.addAtIndex(0,val)
    def addAtTail(self,val):
        self.addAtIndex(self.size,val)
    def addAtIndex(self,index,val):
        if index>self.size:
            return 
        curr = self.head
        new_node =Node(val)
        if index<=0:
            new_node.next = curr
            self.head = new_node
        else:
            for i in range(index-1):
                curr = curr.next
            print(curr.next,curr.val)
            new_node.next = curr.next
            curr.next = new_node 
        self.size = self.size+1
    def print(self):
        curr = self.head
        while curr:
            print(curr.val)
            curr = curr.next
    def middleOfLinkedList(self):
          slow = self.head
          fast = self.head
          while fast and fast.next:
              slow = slow.next
              fast = fast.next.next
          print(slow.val)
    
       
      
         
       
s = LinkedList()
s.addAtHead(4)
s.addAtTail(5)
s.addAtTail(6)
s.addAtTail(7)
#s.addAtHead(8)
s.middleOfLinkedListd()