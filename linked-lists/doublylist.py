class Node:

    def __init__(self, value) -> None:
        self.value = value 
        self.next = None 
        self.prev = None 
    

class DoublyLinkedList:

    def __init__(self) -> None:
        self.head = None 
        self.tail = None 
        self.size = 0 

    
    def setHead(self, node):
    #    if self.head == None:
    #        self.head = node
    #        self.tail = node 
    #    else:
    #        currentHead = self.head 
    #        newHead = node 
    #        newHead.next = currentHead 
    #        self.head = newHead
         pass 

    def setTail(self, node):
        
        # if self.tail == None:
        #     self.tail = node 
        #     self.head = node 
        # # else:
        #     currentTail = self.tail 
        #     newTail = node 
        #     currentTail.next = newTail 
        #     self.tail = newTail 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       currentTail.next = newTail 

    def insertBefore(self, node, nodeToInsert):

        if node == self.head:
        
    def insertAfter(self, node, nodeToInsert):
        # Write your code here.
        pass

    def insertAtPosition(self, position, nodeToInsert):
        # Write your code here.
        pass

    def removeNodesWithValue(self, value):
        # Write your code here.
        pass

    def remove(self, node):
        # Write your code here.
        pass

    def containsNodeWithValue(self, value):
        # Write your code here.
        pass
