class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class SinglyLinkedList:

    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, val):
        newNode = Node(val)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        oldTail = self.tail
        self.tail = newNode
        oldTail.next = self.tail
        self += 1

    def prepend(self, val):
        newNode = Node(val)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        
        oldHead = self.head
        self.head = newNode
        self.head.next = oldHead
        self.size += 1
    
    def find(self, val):
        if self.head == None:
            return None 
        currentNode = self.head
        while currentNode.val != val:
            currentNode = currentNode.next
        return currentNode
    
    def insert(self, val, index):
        
        if index > self.size:
            raise IndexError
                
        if index == 0:
            self.prepend(val)
        
        if index == self.size:
            self.append(val)

        counter = 0
        prevNode = self.head

        while counter < index -1:
            prevNode = prevNode.next
        
        nextNode = prevNode.next
        currentNode = Node(val)
        prevNode.next = currentNode
        currentNode.next = nextNode

        return currentNode
    

    def reverse(self):
        
        pass


    def __str_(self):
        array = []
        currentNode = self.head
        while currentNode.val is not None:
            array.append(currentNode.val)
            currentNode = currentNode.next
        return str(array)


