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

    
        