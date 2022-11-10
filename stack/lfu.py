import collections
class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.prev  = None
        self.next = None
        self.freq = 1
        
class DoublyLinkedList:
    def __init__(self):
        self.head = Node(None,None)
        self.tail = Node(None,None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    def __len__(self):
        return self.size
    def append(self,node):
        prev =self.head.next
        node.prev= self.head
        node.next = prev
        prev.prev = node
        self.head.next = node
        self.size = self.size + 1
    def pop(self,node):
        if self.size == 0:
            return
        if not node:
            pass
        prev =node.prev
        next = node.next
        prev.next = next
        next.prev = prev
        
    
class LFUCache:
    def __init__(self,capacity):
        self.size = 0
        self.capacity = capacity
        self.node = dict()
        self.freq  = collections.defaultdict(DoublyLinkedList)
        self.minfreq = 0
    def update(self,node):
        freq = node.freq
        self.freq[freq].pop(node)
        if self.minfreq == freq and not self.freq[freq]:
            self.minfreq = self.minfreq  +1
        node.freq = node.freq + 1
        freq = node.freq
        self.freq[freq].append(node)
    def get(self,key):
        if key not in self.node:
            return -1
        node = self.node[key]
        self.update(node)
        return node.value
    def put(self,key,value):
        if self.capacity == 0 :
            return 
        
        if key in self.node:
            node = self.node[key]
            self.update(node)
            node.value = value
        else:
            if self.size == self.capacity:
                node = self.freq[self.minfreq].pop()
                del self.node[node.key]
                self.size = self.size - 1
        node = Node(key,value)
        self.node[key] = node
        self.freq[1].append(node)
        self.minfreq = 1
        self.size = self.size+1            
