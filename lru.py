class LRUCache:

    def __init__(self, capacity: int):
        self.hashMap = {}
        self.capacity = capacity 
        self.mostRecent =  DoublyLinkedList()
        

    def get(self, key: int) -> int:
        if key not in self.hashMap:
            return -1 
        keyNode = self.hashMap[key]
        
        self.mostRecent.setHead(keyNode)
        return keyNode.value 
        
        

    def put(self, key: int, value: int) -> None:
        if key in self.hashMap:
            self.mostRecent.setHead(self.hashMap[key])
            return self.hashMap[key].value 
        
        newNode = Node(key, value)
        self.hashMap[key] = newNode 
        self.mostRecent.append(newNode)

        if self.capacity >  self.mostRecent.length:
            self.mostRecent.evictLeastUsed()
        
        

class Node:
    def __init__(self, key, value):
        self.key = key 
        self.value = value 
        self.next = None 
        self.prev = None 
    
    def removeBindings(self, node):
        if node.prev != None:
            prevNode = node.prev 
        if node.next != None:
            nextNode = node.next
        
        node.next = None 
        node.prev = None 
        
        prevNode.next = nextNode 
        
        

class DoublyLinkedList:
    
    def __init__(self):
        self.head = None 
        self.tail = None 
        self.length = 0 
        
    def setHead(self, node):
        if self.head == node:
            return 
        if self.head == None and self.tail == None:
            self.head =  node 
            self.tail = node 
        else:
            node.removeBindings()
            currentHead = self.head
            node.next = currentHead 
            self.head = node 
    
    def append(self, node):
        if self.head != None:
            currentHead = self.head
            node.next = currentHead
            self.head = node 
        else:
            self.head = node 
            self.tail = node 
    
    def evictLeastUsed(self):
        if self.tail != None:
            self.tail.prev = None 
        if self.head == None and self.tail == None:
            return 
            
             
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)