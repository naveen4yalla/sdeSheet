


class DoublyNode:
    def __init__(self,key,value):
        self.value = value
        self.prev = None
        self.next = None
        self.key = key
class lru_cache:
    def __init__(self,size=4):
        self.head = DoublyNode(0,0)
        self.tail = DoublyNode(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = size
        self.count = 0
        self.lrumap = {}
    def put(self,key,value):
        if key  in self.lrumap.keys():
            self.deleteNode(self.lrumap[key])
            del self.lrumap[key]
        if self.count == self.size:
            self.deleteNode(self.tail.prev)
            self.count = self.count -1
        tempNode = DoublyNode(key,value)
        self.addNode(tempNode)
        self.count = self.count + 1
        self.lrumap[tempNode.key] = tempNode
    
    def addNode(self,tempNode):
        prev =self.head.next
        tempNode.prev= self.head
        tempNode.next = prev
        prev.prev = tempNode
        self.head.next = tempNode
       
    def deleteNode(self,tempNode):
        prev =tempNode.prev
        next = tempNode.next
        prev.next = next
        next.prev = prev
    def get(self,key):
        if key not in self.lrumap.keys():
            return -1
        tempNode = self.lrumap[key]
        self.deleteNode(tempNode)
        self.addNode(tempNode) 
        return tempNode.value       
        
            
    
        
    
        