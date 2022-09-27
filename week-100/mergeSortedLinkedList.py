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
def sortedLinkedList(t1,t2):
    printtemp=Node(0)
    head = printtemp
    while True:
        if t1 is None:
            head.next = t2 
            break
        if t2 is None:
            head.next = t1
            break
        if t1.val>=t2.val:
            head.next = t2
            t2 = t2.next
        else:
            head.next = t1
            t1 = t1.next
        head = head.next 
    while printtemp:
        print(printtemp.val)
        printtemp = printtemp.next 
def removenthNodefromEnd(head):
    slow = head
    fast = head 
    for f in range(0,2):
        fast = fast.next
    while fast.next:
        slow = slow.next
        fast = fast.next
    slow.next = fast  



2-3-4-5


        

      
         
       
s = LinkedList()
s.addAtHead(9)
s.addAtHead(8)
s.addAtHead(5)
s.addAtHead(1)

s1 = LinkedList()
s1.addAtHead(11)
s1.addAtHead(4)
s1.addAtHead(3)
s1.addAtHead(2)
sortedLinkedList(s.head,s1.head)