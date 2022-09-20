from ast import Pass
from email import header


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
    def addTwoNumbers(self,s1,s2):
        #create two linked list 
        sumNode = LinkedList()
        returnSumNode= sumNode
        temp1 = s1.head
        temp2 = s2.head
        carry = 0
        while (temp1 or temp2) or carry:
            sum = 0
            if temp1!=None:
                sum  = sum + temp1.val
                temp1 = temp1.next
            if temp1!=None:
                sum  = sum + temp1.val
                temp1 = temp1.next
            
            sum = sum + carry
            carry = sum // 10
            sumNode.next = LinkedList(sum%10)
            sumNode = sumNode.next
        return  returnSumNode.next 
    def deleteNode(self,node):
        node.val = node.next.val
        node.next= node.next.next
    
        
            
           
                
                
        
            
        
        
s = LinkedList()
s.addAtTail(4)
s.addAtTail(5)
s.addAtTAIL(3)
s1= LinkedList()
s.addAtTail(9)
s.addAtTail(9)
s.addAtTail(1)
s.addAtTail(9)
